from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
import models, schemas

#POST valor tienda
def agregar_tienda(db: Session, tienda: schemas.Tienda):
    db_tienda = models.Tienda(
        codigo_tienda = tienda.codigo_tienda,
        nombre_tienda = tienda.nombre_tienda
    )
    db.add(db_tienda)
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

#Get al tienda
def obtener_valores_tienda(db: Session = Depends(SessionLocal)):
    tiendas = db.query(models.Tienda).all()
    return tiendas

#POST valor bebida
def agregar_bebida(db: Session, bebida: schemas.Bebida):
    db_bebida = models.Bebida(
        codigo_bebida = bebida.codigo_bebida,
        nombre_bebida = bebida.nombre_bebida
    )
    db.add(db_bebida)
    db.commit()
    db.refresh(db_bebida)
    return db_bebida

#Get al tienda
def obtener_valores_bebida(db: Session = Depends(SessionLocal)):
    bebidas = db.query(models.Bebida).all()
    return bebidas

#POST valor bebedor
def agregar_bebedor(db: Session, bebedor: schemas.Bebedor):
    db_bebedor = models.Bebedor(
        cedula = bebedor.cedula,
        nombre = bebedor.nombre
    )
    db.add(db_bebedor)
    db.commit()
    db.refresh(db_bebedor)
    return db_bebedor

#Get al tienda
def obtener_valores_bebedor(db: Session = Depends(SessionLocal)):
    bebedores = db.query(models.Bebedor).all()
    return bebedores

#Get al frecuenta 
def obtener_valores_frecuenta(db: Session = Depends(SessionLocal)):
    bebedor = db.query(models.Bebedor).all()
    bebedor = db.query(models.Tienda).all()

    return bebedor

#GET valor bebedores que les gusta cierta bebida
def bebedores_gusta_bebida(db: Session, nombre_bebida: str):
    bebida = db.query(models.Bebida).filter(models.Bebida.nombre_bebida == nombre_bebida).first()
    codigo_bebida = bebida.codigo_bebida
    gusta = db.query(models.Gusta).filter(models.Gusta.codigo_bebida == codigo_bebida).all()
    cedulas = [g.cedula for g in gusta]
    frecuenta = db.query(models.Frecuenta).filter(models.Frecuenta.cedula.in_(cedulas)).all()
    return [f.cedula for f in frecuenta]