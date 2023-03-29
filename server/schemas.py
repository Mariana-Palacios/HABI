from pydantic import BaseModel
#from typing import Dict

class Tienda(BaseModel):
    codigo_tienda: int
    nombre_tienda: str

class Bebida(BaseModel):
    codigo_bebida: int
    nombre_bebida: str

class Bebedor(BaseModel):
    cedula: int
    nombre: str

class Gusta(BaseModel):
    cedula = int
    codigo_bebida = int

class Frecuenta(BaseModel):
    cedula = int
    codigo_tienda = int

class Vende(BaseModel):
    codigo_tienda = int
    codigo_bebida = int
    precio = float