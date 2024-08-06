from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.opinion_cliente
import config.db
import schemas.OpinionCliente
import models.OpinionCliente
from portaortoken import Portador

opinion_router = APIRouter()

# Crea todas las tablas en la base de datos
models.OpinionCliente.Base.metadata.create_all(bind=config.db.engine)

def get_db():
   
    db = config.db.SessionLocal()  # Verifica que SessionLocal esté definido en config.db
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las opiniones de clientes
@opinion_router.get('/opiniones/', response_model=List[schemas.OpinionCliente.OpinionClienteBase], tags=['Opiniones'], dependencies=[Depends(Portador())])
def read_opiniones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
   
    db_opiniones = crud.opinion_cliente.get_opiniones(db=db, skip=skip, limit=limit)
    return db_opiniones

# Ruta para obtener una opinión de cliente por ID
@opinion_router.get('/opiniones/{id}', response_model=schemas.OpinionCliente.OpinionClienteBase, tags=['Opiniones'], dependencies=[Depends(Portador())])
def read_opinion(id: int, db: Session = Depends(get_db)):
   
    db_opinion = crud.opinion_cliente.get_opinion(db=db, id=id)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinión no encontrada")
    return db_opinion

# Ruta para crear una nueva opinión de cliente
@opinion_router.post('/opiniones/', response_model=schemas.OpinionCliente.OpinionClienteBase, tags=['Opiniones'])
def create_opinion(opinion: schemas.OpinionCliente.OpinionClienteCreate, db: Session = Depends(get_db)):
   
    db_opinion = crud.opinion_cliente.get_opinion_by_descripcion(db, descripcion=opinion.descripcion)
    if db_opinion:
        raise HTTPException(status_code=400, detail="Opinión ya existe")
    return crud.opinion_cliente.create_opinion(db=db, opinion=opinion)

# Ruta para actualizar una opinión de cliente existente
@opinion_router.put('/opiniones/{id}', response_model=schemas.OpinionCliente.OpinionClienteBase, tags=['Opiniones'], dependencies=[Depends(Portador())])
def update_opinion(id: int, opinion: schemas.OpinionCliente.OpinionClienteUpdate, db: Session = Depends(get_db)):
    
    db_opinion = crud.opinion_cliente.update_opinion(db=db, id=id, opinion=opinion)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinión no encontrada para actualizar")
    return db_opinion

# Ruta para eliminar una opinión de cliente
@opinion_router.delete('/opiniones/{id}', response_model=schemas.OpinionCliente.OpinionClienteBase, tags=['Opiniones'], dependencies=[Depends(Portador())])
def delete_opinion(id: int, db: Session = Depends(get_db)):
   
    db_opinion = crud.opinion_cliente.delete_opinion(db=db, id=id)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinión no encontrada para eliminar")
    return db_opinion
