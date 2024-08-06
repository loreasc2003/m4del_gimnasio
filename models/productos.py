
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from decimal import *
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Producto(Base):
    __tablename__ = "tbb_productos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    Marca = Column(String(100))
    Cod_barras = Column(String(50))
    Descripcion = Column(String(255))
    Presentacion = Column(String(100))
    Precio_actual = Column(Decimal(6,2))
    Fotografia = Column(String(100))
    Estatus = Column(Boolean, default=False)
    Fecha_registro = Column(DateTime)
    Fecha_actualizacion = Column(DateTime)


