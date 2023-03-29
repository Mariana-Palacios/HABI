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

@app.post("/tienda/")
def agregar_tienda_data(tienda: schemas.Tienda, db: Session = Depends(get_db)):
    return crud.agregar_tienda(db=db, tienda=tienda)

'''
@app.put("/aquarium_data/")
def append_data_aquarium(aquarium: schemas.AquariumParametersIn, db: Session = Depends(get_db)):
    return crud.append_aquarium_data(db=db, aquarium=aquarium)

@app.get("/aquarium_data/")
def get_last_id_aquarium(db: Session = Depends(get_db)):
    return crud.get_aquarium_data(db=db)
'''