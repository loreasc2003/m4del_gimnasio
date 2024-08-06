from sqlalchemy.orm import Session
from models.Pregunta import Pregunta
from schemas.Pregunta import PreguntaCreate, PreguntaUpdate

def get_preguntas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Pregunta).offset(skip).limit(limit).all()

def get_pregunta(db: Session, id: int):
    return db.query(Pregunta).filter(Pregunta.id == id).first()

def get_pregunta_by_pregunta(db: Session, pregunta: str):
    return db.query(Pregunta).filter(Pregunta.pregunta == pregunta).first()

def create_pregunta(db: Session, pregunta: PreguntaCreate):
    db_pregunta = Pregunta(**pregunta.dict())
    db.add(db_pregunta)
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

def update_pregunta(db: Session, id: int, pregunta: PreguntaUpdate):
    db_pregunta = db.query(Pregunta).filter(Pregunta.id == id).first()
    if db_pregunta:
        for key, value in pregunta.dict().items():
            setattr(db_pregunta, key, value)
        db.commit()
        db.refresh(db_pregunta)
    return db_pregunta

def delete_pregunta(db: Session, id: int):
    db_pregunta = db.query(Pregunta).filter(Pregunta.id == id).first()
    if db_pregunta:
        db.delete(db_pregunta)
        db.commit()
    return db_pregunta
