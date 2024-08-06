from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models
import enum
from sqlalchemy import PrimaryKeyConstraint

class UserRol(Base):
    __tablename__ = 'tbd_usuarios_roles'
    Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"))
    Rol_ID = Column(Integer, ForeignKey("tbc_roles.ID"))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    # Definimos la clave primaria compuesta
    __table_args__ = (
        PrimaryKeyConstraint('Usuario_ID', 'Rol_ID'),
    )