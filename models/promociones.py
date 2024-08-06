from sqlalchemy import Column,Boolean, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyTipo(enum.Enum):
    Miembro = "Miembro"
    Empleado = "Empleado"
    Usuario = "Usuario"
    
class MyAplicacion(enum.Enum):
    Tienda_Virtual = "Tienda virtual"
    Tienda_Presencial = "Tienda presencial"

class Promocion(Base):
    __tablename__ = 'tbb_promociones'
    ID = Column(Integer, primary_key=True, index=True)
    Producto_id = Column(Integer, ForeignKey("tbb_productos.ID"))
    Tipo = Column(Enum(MyTipo))
    Aplicacion_en = Column(Enum(MyAplicacion))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    Estatus = Column(Boolean, default=False)