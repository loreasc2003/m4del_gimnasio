from pydantic import BaseModel
from typing import Optional

class OpinionClienteBase(BaseModel):
    descripcion: str
    tipo: Optional[str] = None
    respuesta: Optional[str] = None
    estatus: Optional[bool] = True
    atencion_personal: Optional[str] = None

class OpinionClienteCreate(OpinionClienteBase):
    pass

class OpinionClienteUpdate(OpinionClienteBase):
    descripcion: Optional[str] = None
    tipo: Optional[str] = None
    respuesta: Optional[str] = None
    estatus: Optional[bool] = None
    atencion_personal: Optional[str] = None
