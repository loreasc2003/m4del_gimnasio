from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class PromocionBase(BaseModel):
    Tipo: str
    Aplicacion_en: str
    Estatus: bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
 

class PromocionCreate(PromocionBase):
    pass

class PromocionUpdate(PromocionBase):
    pass

class Promocion(PromocionBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        