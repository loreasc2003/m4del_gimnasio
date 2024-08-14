from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
import enum

class MyTipo(str, enum.Enum):
    Promocion = "Promoción"
    Descuento = "Descuento"
    Precio_Tienda = "Precio Tienda"

class PedidoBase(BaseModel):
    Tipo: MyTipo
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Estatus: bool
    Total_Productos: float
    Costo_Total: float

class PedidoCreate(PedidoBase):
    pass

class PedidoUpdate(PedidoBase):
    pass

class Pedido(PedidoBase):
    ID: int

    class Config:
        orm_mode = True
