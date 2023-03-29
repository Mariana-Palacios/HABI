#from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
#from sqlalchemy.orm import sessionmaker, relationship
#from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

# Definir las clases modelo para cada tabla
class Tienda(Base):
    __tablename__ = 'TIENDA'
    codigo_tienda = Column(Integer, primary_key=True)
    nombre_tienda = Column(String)

class Bebida(Base):
    __tablename__ = 'BEBIDA'
    codigo_bebida = Column(Integer, primary_key=True)
    nombre_bebida = Column(String)

class Bebedor(Base):
    __tablename__ = 'BEBEDOR'
    cedula = Column(Integer, primary_key=True)
    nombre = Column(String)

class Gusta(Base):
    __tablename__ = 'GUSTA'
    cedula = Column(Integer, ForeignKey('BEBEDOR.cedula'), primary_key=True)
    codigo_bebida = Column(Integer, ForeignKey('BEBIDA.codigo_bebida'), primary_key=True)

class Frecuenta(Base):
    __tablename__ = 'FRECUENTA'
    cedula = Column(Integer, ForeignKey('BEBEDOR.cedula'), primary_key=True)
    codigo_tienda = Column(Integer, ForeignKey('TIENDA.codigo_tienda'), primary_key=True)

class Vende(Base):
    __tablename__ = 'VENDE'
    codigo_tienda = Column(Integer, ForeignKey('TIENDA.codigo_tienda'), primary_key=True)
    codigo_bebida = Column(Integer, ForeignKey('BEBIDA.codigo_bebida'), primary_key=True)
    precio = Column(Float)
    
    # Definir la relación entre las tablas VENDE, TIENDA y BEBIDA
    tienda = relationship("Tienda", back_populates="bebidas")
    bebida = relationship("Bebida", back_populates="tiendas")

# Definir la relación inversa entre las tablas VENDE, TIENDA y BEBIDA
Tienda.bebidas = relationship("Vende", back_populates="tienda")
Bebida.tiendas = relationship("Vende", back_populates="bebida")
