from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from fastapi import Depends
from repository import blogRepository

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
    responses={404: {"description": "Not found"}}
)

@router.post('/create-blogs', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blogRepository.create(request, db)

@router.get('/', response_model=list[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    return blogRepository.get_all(db)

@router.get('/{blog_id}', response_model=schemas.ShowBlog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    return blogRepository.get_by_id(blog_id, db)

@router.put('/{blog_id}', response_model=schemas.ShowBlog)
def update_blog(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blogRepository.update(blog_id, request, db)

@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return blogRepository.delete(blog_id, db)  
