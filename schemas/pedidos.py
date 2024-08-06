from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class PedidoBase(BaseModel):
    Tipo: str
    Estatus: bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
 

class PedidoCreate(PedidoBase):
    pass

class PedidoUpdate(PedidoBase):
    pass

class Pedido(PedidoBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        