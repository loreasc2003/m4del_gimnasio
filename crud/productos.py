import models.productos
import schemas.productos
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_producto(db:Session, id: int):
    return db.query(models.productos.Producto).filter(models.productos.Producto.ID == id).first()

# Busqueda por USUARIO
def get_producto_by_nombre(db:Session, nombre: str):
    return db.query(models.productos.Producto).filter(models.productos.Producto.Nombre == nombre).first()

# Buscar todos los nombres
def get_productos(db:Session, skip: int=0, limit:int=10):
    return db.query(models.productos.producto).offset(skip).limit(limit).all()

# Crear nuevo producto
def create_producto(db:Session, producto: schemas.productos.ProductoCreate):
    db_producto = models.productos.Producto(
    Nombre = producto.nombre,
    Marca = producto.Marca,
    Cod_barras = producto.Cod_Barras,
    Descripcion = producto.Descripcion,
    Presentacion = producto.Presentacion,
    Precio_actual = producto. Precio_actual,
    Fotografia = producto. Fotografia,
    Estatus = producto. Estatus,
    Fecha_registro= producto.Fecha_registro,
    Fecha_actualizacion = producto. Fecha_actualizacion)
    
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Actualizar un nombre por id
def update_Producto(db:Session, id:int, Producto:schemas.productos.ProductoUpdate):
    db_producto = db.query(models.productos.Producto).filter(models.productos.Producto.ID == id).first()
    if db_producto:
        for var, value in vars(producto).items():
            setattr(db_producto, var, value) if value else None
        db.commit()
        db.refresh(db_producto)
    return db_producto

# Eliminar un nombre por id
def delete_producto(db:Session, id:int):
    db_producto = db.query(models.productos.producto).filter(models.productos.producto.ID == id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto




