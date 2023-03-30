from pydantic import BaseModel
from typing import Union

#########
#Tienda
#########

# Definir modelo base para la tienda
class TiendaBase(BaseModel):
    codigo_tienda: int
    nombre_tienda:str

# Definir modelo para crear nuevas tiendas
class TiendaCreate(TiendaBase):
    pass

# Definir modelo para leer las tiendas
class Tienda(TiendaBase):
    class Config:
        orm_mode = True

##########
#Bebida
##########

# Definir modelo base para la Bebida
class BebidaBase(BaseModel):
    codigo_bebida: int
    nombre_bebida:str

# Definir modelo para crear nuevas Bebidas
class BebidaCreate(BebidaBase):
    pass

# Definir modelo para leer las Bebidas
class Bebida(BebidaBase):
    class Config:
        orm_mode = True

############
#Bebedor
############

# Definir modelo base para la Bebedor
class BebedorBase(BaseModel):
    cedula: int
    nombre: str

# Definir modelo para crear nuevas Bebedors
class BebedorCreate(BebedorBase):
    pass

# Definir modelo para leer las Bebedors
class Bebedor(BebedorBase):
    class Config:
        orm_mode = True

############
#Gusta
############

# Definir modelo base para la Gusta
class GustaBase(BaseModel):
    cedula: int
    nombre_bebida:Union[str, Bebida]

# Definir modelo para crear nuevas Gustas
class GustaCreate(GustaBase):
    pass

# Definir modelo para leer las Gustas
class Gusta(GustaBase):
    class Config:
        orm_mode = True

############
#Frecuenta
############

# Definir modelo base para la Frecuenta
class FrecuentaBase(BaseModel):
    cedula: int
    codigo_tienda:Union[str, Tienda]

# Definir modelo para crear nuevas Frecuentas
class FrecuentaCreate(FrecuentaBase):
    pass

# Definir modelo para leer las Frecuentas
class Frecuenta(FrecuentaBase):
    class Config:
        orm_mode = True

############
#Vende
############

# Definir modelo base para la Vende
class VendeBase(BaseModel):
    codigo_tienda:Union[str, Tienda]
    codigo_bebida:Union[str, Bebida]
    precio: float

# Definir modelo para crear nuevas Vendes
class VendeCreate(VendeBase):
    pass

# Definir modelo para leer las Vendes
class Vende(VendeBase):
    class Config:
        orm_mode = True