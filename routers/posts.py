from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.post import PostCreate, PostResponse, PostUpdate, PostBase
from models import Post

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/posts/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    try:
        db_post = Post(**post.dict())  # Crear el post con todos los campos, incluyendo user_id
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.get("/posts/user/{user_id}", response_model=List[PostResponse])
def get_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found for this user")
    return posts


@router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.post_id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    for key, value in post_update.dict(exclude_unset=True).items():
        setattr(db_post, key, value)
    
    db.commit()
    db.refresh(db_post)
    return db_post



@router.delete("/posts/{post_id}", response_model=PostResponse)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.post_id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()
    return db_post