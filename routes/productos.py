from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.Producto  # Asegúrate de que el módulo CRUD esté en esta ubicación
import config.db  # Asegúrate de que la configuración de la base de datos esté en esta ubicación
import schemas.Producto  # Asegúrate de que los esquemas estén en esta ubicación
import models.Producto  # Asegúrate de que el modelo Producto esté en esta ubicación
from portaortoken import Portador  # Asegúrate de que Portador esté definido correctamente

producto_router = APIRouter()

# Crea todas las tablas en la base de datos
models.Producto.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()  # Verifica que SessionLocal esté definido en config.db
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los productos
@producto_router.get('/productos/', response_model=List[schemas.Producto.Producto], tags=['Productos'], dependencies=[Depends(Portador())])
def read_productos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_productos = crud.Producto.get_productos(db=db, skip=skip, limit=limit)
    return db_productos

# Ruta para obtener un producto por ID
@producto_router.get('/productos/{id}', response_model=schemas.Producto.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def read_producto(id: int, db: Session = Depends(get_db)):
    db_producto = crud.Producto.get_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# Ruta para crear un producto
@producto_router.post('/productos/', response_model=schemas.Producto.Producto, tags=['Productos'])
def create_producto(producto: schemas.Producto.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.Producto.get_producto_by_cod_barras(db, cod_barras=producto.Cod_barras)
    if db_producto:
        raise HTTPException(status_code=400, detail="Producto con el mismo código de barras ya existe")
    return crud.Producto.create_producto(db=db, producto=producto)

# Ruta para actualizar un producto
@producto_router.put('/productos/{id}', response_model=schemas.Producto.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def update_producto(id: int, producto: schemas.Producto.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = crud.Producto.update_producto(db=db, id=id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado para actualizar")
    return db_producto

# Ruta para eliminar un producto
@producto_router.delete('/productos/{id}', response_model=schemas.Producto.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def delete_producto(id: int, db: Session = Depends(get_db)):
    db_producto = crud.Producto.delete_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado para eliminar")
   





