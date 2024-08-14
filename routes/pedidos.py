from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.pedidos, config.db, schemas.pedidos, models.pedidos
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

pedido_router = APIRouter()
models.pedidos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los pedidos
@pedido_router.get('/pedidos/', response_model=List[schemas.pedidos.Pedido], tags=['Pedidos'],dependencies=[Depends(Portador())])
def read_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_pedidos = crud.pedidos.get_pedidos(db=db, skip=skip, limit=limit)
    return db_pedidos

# Ruta para obtener un pedido por ID
@pedido_router.get('/pedido/{id}', response_model=schemas.pedidos.Pedido, tags=['Pedidos'],dependencies=[Depends(Portador())])
def read_pedido(id: int, db: Session = Depends(get_db)):
    db_pedido = crud.pedidos.get_pedido(db=db, id=id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return db_pedido

# Ruta para crear un pedido
@pedido_router.post('/pedidos/', response_model=schemas.pedidos.Pedido, tags=['Pedidos'])
def create_pedido(pedido: schemas.pedidos.PedidoCreate, db: Session = Depends(get_db)):
    return crud.pedidos.create_pedido(db=db, pedido=pedido)

# Ruta para actualizar un pedido
@pedido_router.put('/pedidos/{id}', response_model=schemas.pedidos.Pedido, tags=['Pedidos'],dependencies=[Depends(Portador())])
def update_pedido(id: int, pedido: schemas.pedidos.PedidoUpdate, db: Session = Depends(get_db)):
    db_pedido = crud.pedidos.update_pedido(db=db, id=id, pedido=pedido)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado, no se pudo actualizar")
    return db_pedido

# Ruta para eliminar un pedido
@pedido_router.delete('/pedidos/{id}', response_model=schemas.pedidos.Pedido, tags=['Pedidos'],dependencies=[Depends(Portador())])
def delete_pedido(id: int, db: Session = Depends(get_db)):
    db_pedido = crud.pedidos.delete_pedido(db=db, id=id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado, no se pudo eliminar")
    return db_pedido
