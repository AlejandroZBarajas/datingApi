from pydantic import BaseModel

class PostBase(BaseModel):
    titulo: str
    descripcion: str
    duracion: str
    costo: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    post_id: int

    class Config:
        orm_mode = True
