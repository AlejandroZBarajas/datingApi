from fastapi import FastAPI
from routers import users, posts, citas
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

#uvicorn main:app  --reload --host 0.0.0.0 --port 8000

origins = [
    "*"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,  # Permite todas las direcciones. Cambia esto en producción.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(citas.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Itsadate API!"}

