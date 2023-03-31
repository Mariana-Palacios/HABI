from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
import models, schemas
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import aliased

'''
Tienda
'''

#POST valor TIENDA
def agregar_tienda(db: Session, tienda: schemas.TiendaCreate):
    db_tienda = models.Tienda(
        codigo_tienda = tienda.codigo_tienda,
        nombre_tienda = tienda.nombre_tienda
    )
    db.add(db_tienda)
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

#GET al TIENDA
def obtener_valores_tienda(db: Session = Depends(SessionLocal)):
    tiendas = db.query(models.Tienda).all()
    return tiendas

'''
Bebida
'''


#POST valor BEBIDA
def agregar_bebida(db: Session, bebida: schemas.BebidaCreate):
    db_bebida = models.Bebida(
        codigo_bebida = bebida.codigo_bebida,
        nombre_bebida = bebida.nombre_bebida
    )
    db.add(db_bebida)
    db.commit()
    db.refresh(db_bebida)
    return db_bebida

#GET al BEBIDA
def obtener_valores_bebida(db: Session = Depends(SessionLocal)):
    bebidas = db.query(models.Bebida).all()
    return bebidas

'''
Bebedor
'''

#POST valor BEBEDOR
def agregar_bebedor(db: Session, bebedor: schemas.BebedorCreate):
    db_bebedor = models.Bebedor(
        cedula = bebedor.cedula,
        nombre = bebedor.nombre
    )
    db.add(db_bebedor)
    db.commit()
    db.refresh(db_bebedor)
    return db_bebedor

#GET al BEBEDOR
def obtener_valores_bebedor(db: Session = Depends(SessionLocal)):
    bebedores = db.query(models.Bebedor).all()
    return bebedores

'''
Frecuenta
'''

#POST al FRECUENTA
def agregar_frecuenta(db: Session, frecuenta: schemas.FrecuentaCreate):
    db_frecuenta = models.Frecuenta(
        cedula = frecuenta.cedula,
        codigo_tienda = frecuenta.codigo_tienda
    )
    db.add(db_frecuenta)
    db.commit()
    db.refresh(db_frecuenta)
    return db_frecuenta


#GET al FRECUENTA
def obtener_valores_frecuenta(db: Session = Depends(SessionLocal)):
    frecuenta = db.query(models.Frecuenta).all()
    return frecuenta


'''
Vende
'''

#POST al vende
def agregar_vende(db: Session, vende: schemas.VendeCreate):
    db_vende = models.Vende(
        codigo_tienda = vende.codigo_tienda,
        codigo_bebida = vende.codigo_bebida,
        precio = vende.precio
    )
    db.add(db_vende)
    db.commit()
    db.refresh(db_vende)
    return db_vende


#GET al vende
def obtener_valores_vende(db: Session = Depends(SessionLocal)):
    vende = db.query(models.Vende).all()
    return vende

'''
Gusta
'''

#POST al GUSTA
def agregar_gusta(db: Session, gusta: schemas.GustaCreate):
    db_gusta = models.Gusta(
        cedula = gusta.cedula,
        codigo_bebida = gusta.codigo_bebida
    )
    db.add(db_gusta)
    db.commit()
    db.refresh(db_gusta)
    return db_gusta


#GET al GUSTA
def obtener_valores_gusta(db: Session = Depends(SessionLocal)):
    gusta = db.query(models.Gusta).all()
    return gusta


'''
-Los bebedores que frecuentan solo las tiendas que frecuenta Luis Perez.

'''

#1-Los bebedores que no les gusta la colombiana.
def gusta_colombiana(db: Session):
    query = db.query(models.Gusta, models.Bebedor, models.Bebida).\
            join(models.Bebedor, models.Bebedor.cedula == models.Gusta.cedula).\
            join(models.Bebida, models.Bebida.codigo_bebida == models.Gusta.codigo_bebida).\
            filter(models.Bebida.nombre_bebida != "Colombiana").all()
    results = []
    for gusto, bebedor, bebida in query:
        result = {
            "nombre": bebedor.nombre,
            "nombre_bebida": bebida.codigo_bebida
        }
        results.append(result)

    return results

#2-Las fuentes de soda que no son frecuentadas por Andres Camilo Restrepo.

def frecuenta_Andres(db: Session):
    query = db.query(models.Bebedor, models.Frecuenta, models.Tienda).\
            join(models.Frecuenta, models.Frecuenta.cedula == models.Bebedor.cedula).\
            join(models.Tienda, models.Tienda.codigo_tienda == models.Frecuenta.codigo_tienda).\
            filter(models.Bebedor.nombre == "Andres Camilo Restrepo").all()
    results = []
    for bebedor, frecuenta, tienda in query:
        result = {
            "nombre": bebedor.nombre,
            "nombre_bebida": tienda.nombre_tienda
        }
        results.append(result)

    return results

#3-Los bebedores que les gusta al menos una bebida y que frecuentan al menos una tienda.

def gusta_bebita_tienda(db: Session):
    queryBebedor = db.query(models.Bebedor, models.Frecuenta).\
            join(models.Frecuenta, models.Frecuenta.cedula == models.Bebedor.cedula).all()
    queryGusta = db.query(models.Bebedor, models.Gusta).\
            join(models.Gusta, models.Gusta.cedula == models.Bebedor.cedula).all()
    results = []
    for bebedor,frecuenta in queryBebedor:
        results.append({"name":bebedor.nombre})
    for bebedor,gusta in queryGusta:
        results.append({"name":bebedor.nombre})

    return results


#4-Para cada bebedor, las bebidas que no le gustan.

def bebida_no_gusta(db: Session):
    query = db.query(models.Bebedor, models.Gusta, models.Bebida).\
            join(models.Gusta, models.Gusta.cedula == models.Bebedor.cedula).\
            join(models.Bebida, models.Bebida.codigo_bebida == models.Gusta.codigo_bebida).all()
    results = []
    bebidas_todas = db.query(models.Bebida).all()
    bebidas = []
    for bebida in bebidas_todas:
        bebidas.append(bebida.nombre_bebida)
    
    print(bebidas)
    for bebedor, gusta, bebida in query:
        result = {
            "nombre": bebedor.nombre,
            "nombre_bebidas": [elemento for elemento in bebidas if elemento != bebida.nombre_bebida]
        }
        results.append(result)

    return results

#5-Los bebedores que frecuentan solo las tiendas que frecuenta Luis Perez.



#6-Los bebedores que unicamente frecuentan las tiendas que unicamente sirven alguna bebida que le gusta.

def frecuenta_tienda_bebida_gusta(db: Session):
    frec_gusta = aliased(models.Frecuenta)
    bebedor = aliased(models.Bebedor)
    query = db.query(models.Bebedor, models.Frecuenta, models.Tienda, models.Bebida, models.Gusta).\
        join(models.Bebedor, models.Bebedor.cedula == models.Frecuenta.cedula).\
        join(models.Frecuenta, models.Frecuenta.codigo_tienda == models.Tienda.codigo_tienda).\
        join(models.Bebedor, models.Bebedor.cedula == models.Gusta.cedula).\
        join(models.Gusta, models.Gusta.codigo_bebida == models.Bebida.codigo_bebida).\
        join(frec_gusta, frec_gusta.cedula == models.Gusta.cedula).all()
    results = []
    for bebedor, frecuenta, tienda, bebida, gusta in query :
        result = {
            "nombre": bebedor.nombre
        }
        results.append(result)
    return results
