import models.promociones
import schemas.promociones
from sqlalchemy.orm import Session

# Búsqueda por id
def get_promocion(db: Session, id: int):
    return db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()

# Buscar todas las promociones
def get_promociones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.promociones.Promocion).offset(skip).limit(limit).all()

# Crear una nueva promoción
# Crear una nueva promoción
def create_promocion(db: Session, promocion: schemas.promociones.PromocionCreate):
    db_promocion = models.promociones.Promocion(
        Tipo=promocion.Tipo,
        Aplicacion_en=promocion.Aplicacion_en,  # Asegúrate de que esto sea un valor del Enum
        Fecha_Registro=promocion.Fecha_Registro,
        Fecha_Actualizacion=promocion.Fecha_Actualizacion,
        Estatus=promocion.Estatus
    )
    db.add(db_promocion)
    db.commit()
    db.refresh(db_promocion)
    return db_promocion


# Actualizar una promoción por id
def update_promocion(db: Session, id: int, promocion: schemas.promociones.PromocionUpdate):
    db_promocion = db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()
    if db_promocion:
        for var, value in vars(promocion).items():
            if value is not None:
                setattr(db_promocion, var, value)
        db.commit()
        db.refresh(db_promocion)
    return db_promocion

# Eliminar una promoción por id
def delete_promocion(db: Session, id: int):
    db_promocion = db.query(models.promociones.Promocion).filter(models.promociones.Promocion.ID == id).first()
    if db_promocion:
        db.delete(db_promocion)
        db.commit()
    return db_promocion
