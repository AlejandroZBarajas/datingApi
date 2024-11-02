from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.cita import CitaCreate, CitaResponse
from models import Cita

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/citas/", response_model=CitaResponse)
def create_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    db_cita = Cita(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita
