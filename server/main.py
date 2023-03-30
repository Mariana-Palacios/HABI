from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#React
origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#tienda

@app.post("/tienda/", response_model=schemas.Tienda)
def agregar_tienda_data(tienda: schemas.Tienda, db: Session = Depends(get_db)):
    return crud.agregar_tienda(db=db, tienda=tienda)


@app.get("/tienda/")
def obtener_tiendas(db: Session = Depends(get_db)):
    return crud.obtener_valores_tienda(db=db)


@app.get("/testing_def/")
def testing_def(db: Session = Depends(get_db)):
    crud.gusta_colombiana(db=db)
    return {"nombre": "momda"}


#bedida

@app.post("/bebida/")
def agregar_bebida_data(bebida: schemas.Bebida, db: Session = Depends(get_db)):
    return crud.agregar_bebida(db=db, bebida=bebida)


@app.get("/bebida/")
def obtener_valores_bebida_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_bebida(db=db)

#bebedor

@app.post("/bebedor/")
def agregar_bebedor_data(bebedor: schemas.Bebedor, db: Session = Depends(get_db)):
    return crud.agregar_bebedor(db=db, bebedor=bebedor)

@app.get("/bebedor/")
def obtener_valores_bebedor_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_bebedor(db=db)

#gusta

@app.post("/gusta/")
def agregar_gusta_data(gusta: schemas.Gusta, db: Session = Depends(get_db)):
    return crud.agregar_gusta(db=db, gusta = gusta)

@app.get("/gusta/")
def obtener_valores_gusta_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_gusta(db=db)

#frecuenta

@app.post("/frecuenta/")
def obtener_valores_frecuenta_todo(frecuenta: schemas.Frecuenta, db: Session = Depends(get_db)):
    return crud.obtener_valores_frecuenta(db=db, frecuenta = frecuenta)

@app.get("/frecuenta/")
def obtener_valores_frecuenta_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_frecuenta(db=db)

#vende

@app.post("/vende/")
def agregar_vende_data(vende: schemas.Vende, db: Session = Depends(get_db)):
    return crud.agregar_vende(db=db, vende=vende)

@app.get("/vende/")
def obtener_valores_vende_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_vende(db=db)

#-Los bebedores que no les gusta la colombiana.

@app.get("/bebedorGustaColombiana/")
def obtener_valores_vende_todo(db: Session = Depends(get_db)):
    return crud.obtener_valores_vende(db=db)

@app.get("/tienda/")
def get_last_id_aquarium(db: Session = Depends(get_db)):
    return crud.obtener_valores_tienda(db=db)
