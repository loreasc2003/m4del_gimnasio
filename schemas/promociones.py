from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import enum

class MyTipo(str, enum.Enum):
    Miembro = "Miembro"
    Empleado = "Empleado"
    Usuario = "Usuario"

class MyAplicacion(str, enum.Enum):
    Tienda_Virtual = "Tienda virtual"
    Tienda_Presencial = "Tienda presencial"

class PromocionBase(BaseModel):
    Tipo: MyTipo
    Aplicacion_en: MyAplicacion
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Estatus: bool

class PromocionCreate(PromocionBase):
    pass

class PromocionUpdate(BaseModel):
    Tipo: Optional[MyTipo] = None
    Aplicacion_en: Optional[MyAplicacion] = None
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None
    Estatus: Optional[bool] = None

class Promocion(PromocionBase):
    ID: int

    class Config:
        orm_mode = True
