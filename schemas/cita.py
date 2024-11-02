from pydantic import BaseModel

class CitaBase(BaseModel):
    accompanied: int
    post: int

class CitaCreate(CitaBase):
    pass

class CitaResponse(CitaBase):
    cita_id: int

    class Config:
        orm_mode = True
