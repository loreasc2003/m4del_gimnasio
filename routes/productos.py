from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.productos  
import config.db 
import schemas.productos 
import models.productos  
from portaortoken import Portador  

producto_router = APIRouter()

# Crea todas las tablas en la base de datos
models.productos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()  # Verifica que SessionLocal esté definido en config.db
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los productos
@producto_router.get('/productos/', response_model=List[schemas.productos.Producto], tags=['Productos'], dependencies=[Depends(Portador())])
def read_productos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_productos = crud.productos.get_productos(db=db, skip=skip, limit=limit)
    return db_productos

# Ruta para obtener un producto por ID
@producto_router.get('/productos/{id}', response_model=schemas.productos.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def read_producto(id: int, db: Session = Depends(get_db)):
    db_producto = crud.productos.get_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# Ruta para crear un producto
@producto_router.post('/productos/', response_model=schemas.productos.Producto, tags=['Productos'])
def create_producto(producto: schemas.productos.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.productos.get_producto_by_cod_barras(db, cod_barras=producto.Cod_barras) 
    if db_producto:
        raise HTTPException(status_code=400, detail="Producto con el mismo código de barras ya existe")
    return crud.productos.create_producto(db=db, producto=producto)
# Ruta para actualizar un producto
@producto_router.put('/productos/{id}', response_model=schemas.productos.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def update_producto(id: int, producto: schemas.productos.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = crud.productos.update_producto(db=db, id=id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado para actualizar")
    return db_producto

# Ruta para eliminar un producto
@producto_router.delete('/productos/{id}', response_model=schemas.productos.Producto, tags=['Productos'], dependencies=[Depends(Portador())])
def delete_producto(id: int, db: Session = Depends(get_db)):
    db_producto = crud.productos.delete_producto(db=db, id=id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado para eliminar")
   





