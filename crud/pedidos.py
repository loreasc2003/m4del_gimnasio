import models.pedidos
import schemas.pedidos
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_pedido(db:Session, id: int):
    return db.query(models.pedidos.Pedido
                    ).filter(models.pedidos.Pedido.ID == id).first()

# Busqueda por Nombre
def get_pedido_by_tipo(db:Session, tipo: str):
    return db.query(models.pedidos.Pedido).filter(models.pedidos.Pedidos.Tipo == tipo).first()

# Buscar todos las personas
def get_pedidos(db:Session, skip: int=0, limit:int=10):
    return db.query(models.pedidos.Pedido).offset(skip).limit(limit).all()

# Crear una nueva personas
def create_pedido(db:Session, pedido: schemas.pedidos.PedidoCreate):
    db_pedido = models.pedidos.Pedido(Tipo = pedido.Tipo,
                                    Estatus = pedido.Estatus,
                                    Fecha_Registro = pedido.Fecha_Registro,
                                    Fecha_Actualizacion = pedido.Fecha_Actualizacion)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Actualizar una personas por id
def update_person(db:Session, id:int, person:schemas.pedidos.PedidoUpdate):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        for var, value in vars(person).items():
            setattr(db_pedido, var, value) if value else None
        db.commit()
        db.refresh(db_pedido)
    return db_pedido

# Eliminar una personas por id
def delete_pedido(db:Session, id:int):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
    return db_pedido

