from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(45), nullable=False)
    passwrd = Column(String(45), nullable=False)
    nombres = Column(String(45), nullable=False)
    apellidoP = Column(String(45), nullable=False)
    apellidoM = Column(String(45), nullable=False)
    sexo = Column(Enum('Hombre', 'Mujer'), nullable=False)
    rol = Column(Enum('Companion', 'Accompanied'), nullable=False)

    posts = relationship("Post", back_populates="owner")
    citas = relationship("Cita", back_populates="accompanied_user")

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(45), nullable=False)
    descripcion = Column(String(45), nullable=False)
    duracion = Column(String(45), nullable=False)
    costo = Column(String(45), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    owner = relationship("User", back_populates="posts")

class Cita(Base):
    __tablename__ = "citas"

    cita_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    accompanied = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    post = Column(Integer, ForeignKey("posts.post_id"), nullable=False)

    accompanied_user = relationship("User", back_populates="citas")
    post_relation = relationship("Post")
