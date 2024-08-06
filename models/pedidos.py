from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum, Float
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyTipo(enum.Enum):
    Promocion = "Promoción"
    Descuento = "Descuento"
    Precio_Tienda = "Precio Tienda"

class Pedido(Base):
    __tablename__ = 'tbb_pedidos'
    ID = Column(Integer, primary_key=True, index=True)
    Producto_id = Column(Integer, ForeignKey("tbb_productos.ID"))
    Usuario_id = Column(Integer, ForeignKey("tbb_usuarios.ID"))
    Tipo = Column(Enum(MyTipo))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean, default=False)
    Total_Productos = Column(Float)
    Costo_Total = Column(Float)