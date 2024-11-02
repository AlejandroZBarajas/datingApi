from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user import UserCreate, UserResponse, UserLogin
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
    return db_user

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Buscar el usuario por su nombre
    db_user = db.query(User).filter(User.username == user.username).first()
    
    # Verificar si el usuario existe y si la contraseña es correcta
    if db_user and db_user.passwrd == user.passwrd:  # Comparación con la columna correcta
        return {"role": db_user.rol, "user_id": db_user.user_id}  # Asegúrate de que estos sean los atributos correctos
    
    # Lanzar excepción HTTP 401 si las credenciales son inválidas
    raise HTTPException(status_code=401, detail="Invalid credentials")