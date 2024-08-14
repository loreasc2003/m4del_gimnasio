from sqlalchemy import Column, Boolean, Integer, DateTime, Enum
from sqlalchemy.sql import func
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
    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Tipo = Column(Enum(MyTipo), nullable=False)
    Aplicacion_en = Column(Enum(MyAplicacion), nullable=False)
    Fecha_Registro = Column(DateTime, server_default=func.now())
    Fecha_Actualizacion = Column(DateTime, onupdate=func.now())
    Estatus = Column(Boolean, default=False)
