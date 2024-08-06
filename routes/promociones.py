from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.promociones, config.db, schemas.promociones, models.promociones
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

promocion = APIRouter()
models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Personas
@promocion.get('/promociones/', response_model=List[schemas.promociones.Promocion],tags=['Promociones'],dependencies=[Depends(Portador())])
def read_promociones(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_promociones = crud.promociones.get_promociones(db=db,skip=skip, limit=limit)
    return db_promociones

# Ruta para obtener un Persona por ID
@promocion.post("/person/{id}", response_model=schemas.promociones.Promocion, tags=["Promociones"], dependencies=[Depends(Portador())])
def read_promociones(id: int, db: Session = Depends(get_db)):
    db_promociones= crud.promociones.get_promociones(db=db, id=id)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="Promoción not found")
    return db_promociones

# Ruta para crear un usurio
@promocion.post('/promociones/', response_model=schemas.promociones.Promocion,tags=['Promociones'])
def create_promociones(promocion: schemas.promociones.PromocionCreate, db: Session=Depends(get_db)):
    db_promociones = crud.promociones.get_promocion_by_tipo(db,tipo=promocion.tipo)
    if db_promociones:
        raise HTTPException(status_code=400, detail="Promociones existente intenta nuevamente")
    return crud.promociones.create_promocion(db=db, promocion=promocion)

# Ruta para actualizar un Persona
@promocion.put('/promociones/{id}', response_model=schemas.promociones.Promocion,tags=['Promociones'], dependencies=[Depends(Portador())])
def update_promociones(id:int,promocion: schemas.promociones.PromocionUpdate, db: Session=Depends(get_db)):
    db_promociones = crud.promociones.update_promocion(db=db, id=id, promocion=promocion)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="Promociones no existe, no se pudo actualizar ")
    return db_promociones

# Ruta para eliminar un Persona
@promocion.delete('/promociones/{id}', response_model=schemas.promociones.Promocion,tags=['Promociones'], dependencies=[Depends(Portador())])
def delete_promociones(id:int, db: Session=Depends(get_db)):
    db_promociones = crud.promociones.delete_promociones(db=db, id=id)
    if db_promociones is None:
        raise HTTPException(status_code=404, detail="Promociones no existe, no se pudo eliminar ")
    return db_promociones