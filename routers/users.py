from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user import UserCreate, UserResponse, UserLogin, UsertoEdit
from models import User
from pydantic import BaseModel

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"role": db_user.rol, "user_id": db_user.user_id, "username": db_user.username}

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user and db_user.passwrd == user.passwrd: 
        return {"role": db_user.rol, "user_id": db_user.user_id, "username": db_user.username}  

    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/users/{user_id}/", response_model=UsertoEdit)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsertoEdit(
        user_id=db_user.user_id,
        username=db_user.username,
        nombres=db_user.nombres,
        apellidoP=db_user.apellidoP,
        apellidoM=db_user.apellidoM,
        sexo=db_user.sexo
    )