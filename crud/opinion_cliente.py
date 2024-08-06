from sqlalchemy.orm import Session
from models.OpinionCliente import OpinionCliente
from schemas.OpinionCliente import OpinionClienteCreate, OpinionClienteUpdate

def get_opiniones(db: Session, skip: int = 0, limit: int = 10):
    
    return db.query(OpinionCliente).offset(skip).limit(limit).all()

def get_opinion(db: Session, id: int):
   
    return db.query(OpinionCliente).filter(OpinionCliente.id == id).first()

def get_opinion_by_descripcion(db: Session, descripcion: str):
   
    return db.query(OpinionCliente).filter(OpinionCliente.descripcion == descripcion).first()

def create_opinion(db: Session, opinion: OpinionClienteCreate):
   
    db_opinion = OpinionCliente(**opinion.dict())
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)
    return db_opinion

def update_opinion(db: Session, id: int, opinion: OpinionClienteUpdate):
  
    db_opinion = db.query(OpinionCliente).filter(OpinionCliente.id == id).first()
    if db_opinion:
        for key, value in opinion.dict().items():
            setattr(db_opinion, key, value)
        db.commit()
        db.refresh(db_opinion)
    return db_opinion

def delete_opinion(db: Session, id: int):
 
    db_opinion = db.query(OpinionCliente).filter(OpinionCliente.id == id).first()
    if db_opinion:
        db.delete(db_opinion)
        db.commit()
    return db_opinion
