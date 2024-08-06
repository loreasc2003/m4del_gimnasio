from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.pedidos, config.db, schemas.pedidos, models.pedidos
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

pedido = APIRouter()
models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Pedidos
@pedido.get('/pedidos/', response_model=List[schemas.pedidos.Pedido],tags=['Pedidos'],dependencies=[Depends(Portador())])
def read_pedidos(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_pedidos = crud.pedidos.get_pedidos(db=db,skip=skip, limit=limit)
    return db_pedidos

# Ruta para obtener un Pedido por ID
@pedido.post("/pedido/{id}", response_model=schemas.pedidos.Pedido, tags=["Pedidos"], dependencies=[Depends(Portador())])
def read_pedidos(id: int, db: Session = Depends(get_db)):
    db_pedido= crud.pedidos.get_pedido(db=db, id=id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return db_pedido

# Ruta para crear un pedido
@pedido.post('/pedidos/', response_model=schemas.pedidos.Pedido,tags=['Pedidos'])
def create_pedidos(pedido: schemas.pedidos.PedidoCreate, db: Session=Depends(get_db)):
    db_pedidos = crud.pedidos.get_pedido_by_tipo(db,tipo=pedido.tipo)
    if db_pedidos:
        raise HTTPException(status_code=400, detail="Pedido existente intenta nuevamente")
    return crud.pedidos.create_pedidos(db=db, pedido=pedido)

# Ruta para actualizar un Persona
@pedido.put('/pedidos/{id}', response_model=schemas.pedidos.Pedido,tags=['Pedidos'], dependencies=[Depends(Portador())])
def update_pedidos(id:int,pedido: schemas.pedidos.PedidoUpdate, db: Session=Depends(get_db)):
    db_pedidos = crud.pedidos.update_pedidos(db=db, id=id, pedido=pedido)
    if db_pedidos is None:
        raise HTTPException(status_code=404, detail="Pedido no existe, no se pudo actualizar ")
    return db_pedidos

# Ruta para eliminar un pedido
@pedido.delete('/pedidos/{id}', response_model=schemas.pedidos.Pedido,tags=['Pedidos'], dependencies=[Depends(Portador())])
def delete_pedidos(id:int, db: Session=Depends(get_db)):
    db_pedidos = crud.pedidos.delete_pedidos(db=db, id=id)
    if db_pedidos is None:
        raise HTTPException(status_code=404, detail="Pedido no existe, no se pudo eliminar ")
    return db_pedidos