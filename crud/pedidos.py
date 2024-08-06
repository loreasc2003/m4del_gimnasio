import models.pedidos
import schemas.pedidos
import models.users
import schemas.users
from sqlalchemy.orm import Session
from sqlalchemy import and_

# Buscar pedido por id
def get_pedido(db: Session, id: int):
    return db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()

# Buscar pedido por tipo
def get_pedido_by_tipo(db: Session, tipo: str):
    return db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.Tipo == tipo).first()

# Buscar usuario por credenciales
def get_user_by_credentials(db: Session, username: str, correo: str, telefono: str, password: str):
    return db.query(models.users.User).filter(
        and_(
            (models.users.User.Nombre_Usuario == username),
            (models.users.User.Correo_Electronico == correo),
            (models.users.User.Numero_Telefonico_Movil == telefono),
            (models.users.User.Contrasena == password)
        )
    ).first()

# Buscar todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Crear nuevo pedido
def create_pedido(db: Session, pedido: schemas.pedidos.PedidoCreate):
    db_pedido = models.pedidos.Pedido(
        Tipo=pedido.Tipo,
        Estatus=pedido.Estatus,
        Fecha_Registro=pedido.Fecha_Registro,
        Fecha_Actualizacion=pedido.Fecha_Actualizacion
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Actualizar un pedido por id
def update_pedido(db: Session, id: int, pedido: schemas.pedidos.PedidoUpdate):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        for var, value in vars(pedido).items():
            if value is not None:  # Solo actualizar si el valor no es None
                setattr(db_pedido, var, value)
        db.commit()
        db.refresh(db_pedido)
    return db_pedido

# Eliminar un pedido por id
def delete_pedido(db: Session, id: int):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
    return db_pedido

