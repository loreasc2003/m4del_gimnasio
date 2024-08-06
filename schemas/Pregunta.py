from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PreguntaBase(BaseModel):
    pregunta: str
    respuesta: str
    categoria: Optional[str] = None
    persona: Optional[str] = None
    estatus: Optional[bool] = True

class PreguntaCreate(PreguntaBase):
    pass

class PreguntaUpdate(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
