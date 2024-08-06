from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
import crud.Pregunta  
import config.db  
import schemas.Pregunta  
import models.Pregunta  
from portaortoken import Portador 

pregunta_router = APIRouter()

# Crea todas las tablas en la base de datos
models.Pregunta.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()  # Verifica que SessionLocal esté definido en config.db
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las preguntas
@pregunta_router.get('/preguntas/', response_model=List[schemas.Pregunta.Pregunta], tags=['Preguntas'], dependencies=[Depends(Portador())])
def read_preguntas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_preguntas = crud.Pregunta.get_preguntas(db=db, skip=skip, limit=limit)
    return db_preguntas

# Ruta para obtener una pregunta por ID
@pregunta_router.get('/preguntas/{id}', response_model=schemas.Pregunta.Pregunta, tags=['Preguntas'], dependencies=[Depends(Portador())])
def read_pregunta(id: int, db: Session = Depends(get_db)):
    db_pregunta = crud.Pregunta.get_pregunta(db=db, id=id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return db_pregunta

# Ruta para crear una pregunta
@pregunta_router.post('/preguntas/', response_model=schemas.Pregunta.Pregunta, tags=['Preguntas'])
def create_pregunta(pregunta: schemas.Pregunta.PreguntaCreate, db: Session = Depends(get_db)):
    db_pregunta = crud.Pregunta.get_pregunta_by_pregunta(db, pregunta=pregunta.pregunta)
    if db_pregunta:
        raise HTTPException(status_code=400, detail="Pregunta ya existe")
    return crud.Pregunta.create_pregunta(db=db, pregunta=pregunta)

# Ruta para actualizar una pregunta
@pregunta_router.put('/preguntas/{id}', response_model=schemas.Pregunta.Pregunta, tags=['Preguntas'], dependencies=[Depends(Portador())])
def update_pregunta(id: int, pregunta: schemas.Pregunta.PreguntaUpdate, db: Session = Depends(get_db)):
    db_pregunta = crud.Pregunta.update_pregunta(db=db, id=id, pregunta=pregunta)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada para actualizar")
    return db_pregunta

# Ruta para eliminar una pregunta
@pregunta_router.delete('/preguntas/{id}', response_model=schemas.Pregunta.Pregunta, tags=['Preguntas'], dependencies=[Depends(Portador())])
def delete_pregunta(id: int, db: Session = Depends(get_db)):
    db_pregunta = crud.Pregunta.delete_pregunta(db=db, id=id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada para eliminar")
    return db_pregunta
