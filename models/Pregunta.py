from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime

Base = declarative_base()

class Pregunta(Base):
    __tablename__ = 'tbc_preguntas'
    
    id = Column(Integer, primary_key=True, index=True)
    pregunta = Column(String(255), nullable=False)
    respuesta = Column(LONGTEXT, nullable=False)
    categoria = Column(String(100))
    persona = Column(String(100))
    estatus = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, onupdate=datetime.utcnow)
    
  #  def __repr__(self):
   #     return (f"<Pregunta(id={self.id}, pregunta='{self.pregunta}', "
    #            f"respuesta='{self.respuesta[:20]}...', categoria='{self.categoria}', "
     #           f"persona='{self.persona}', estatus={self.estatus})>")
