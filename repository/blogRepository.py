
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    
    new_blog = models.Blog(
        title=request.title, 
        body=request.body,
        user_id=1  
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_by_id(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog

def update(blog_id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog

def delete(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    db.delete(blog)
    db.commit()
    return None  # For 204 No Content response