from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    titulo: str
    descripcion: str
    duracion: str
    costo: str

class PostCreate(PostBase):
    titulo:str
    descripcion:str
    duracion:str
    costo:str
    user_id: int
    pass

class PostResponse(PostBase):
    post_id: int

    class Config:
        orm_mode = True

class PostUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    duracion: Optional[str] = None
    costo: Optional[str] = None

    class Config:
        orm_mode = True