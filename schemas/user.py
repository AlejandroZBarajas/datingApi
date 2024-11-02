from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    passwrd: str
    nombres: str
    apellidoP: str
    apellidoM: str
    sexo: str
    rol: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    username: str
    nombres: str
    apellidoP: str
    apellidoM: str
    sexo: str
    rol: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    passwrd: str

class UsertoEdit(BaseModel):
    user_id: int
    username: str
    nombres: str
    apellidoP: str
    apellidoM: str
    sexo: str

    class Config:
        orm_mode = True
    