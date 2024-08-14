from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.promociones, config.db, schemas.promociones, models.promociones
from typing import List
from portadortoken import Portador

# Si no usas la clave de cifrado, puedes eliminar esta sección
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# f = Fernet(key)

promocion_router = APIRouter()
models.promociones.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todas las promociones
@promocion_router.get('/promociones/', response_model=List[schemas.promociones.Promocion], tags=['Promociones'], dependencies=[Depends(Portador())])
def read_promociones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_promociones = crud.promociones.get_promociones(db=db, skip=skip, limit=limit)
    return db_promociones

# Ruta para obtener una promoción por ID
@promocion_router.get('/promocion/{id}', response_model=schemas.promociones.Promocion, tags=['Promociones'], dependencies=[Depends(Portador())])
def read_promocion(id: int, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.get_promocion(db=db, id=id)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada")
    return db_promocion

# Ruta para crear una promoción
@promocion_router.post('/promociones/', response_model=schemas.promociones.Promocion, tags=['Promociones'])
def create_promocion(promocion: schemas.promociones.PromocionCreate, db: Session = Depends(get_db)):
    return crud.promociones.create_promocion(db=db, promocion=promocion)

# Ruta para actualizar una promoción
@promocion_router.put('/promociones/{id}', response_model=schemas.promociones.Promocion, tags=['Promociones'], dependencies=[Depends(Portador())])
def update_promocion(id: int, promocion: schemas.promociones.PromocionUpdate, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.update_promocion(db=db, id=id, promocion=promocion)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada, no se pudo actualizar")
    return db_promocion

# Ruta para eliminar una promoción
@promocion_router.delete('/promociones/{id}', response_model=schemas.promociones.Promocion, tags=['Promociones'], dependencies=[Depends(Portador())])
def delete_promocion(id: int, db: Session = Depends(get_db)):
    db_promocion = crud.promociones.delete_promocion(db=db, id=id)
    if db_promocion is None:
        raise HTTPException(status_code=404, detail="Promoción no encontrada, no se pudo eliminar")
    return db_promocion
