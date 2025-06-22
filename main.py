from fastapi import FastAPI , status
import uvicorn
import models
from database import engine
from sqlalchemy.orm import Session
from database import SessionLocal
app = FastAPI()
from fastapi import Depends
import schemas
from database import get_db
from passlib.context import CryptContext
from fastapi import HTTPException
models.Base.metadata.create_all(bind=engine)


@app.post('/blogs/', status_code= status.HTTP_201_CREATED, response_model=schemas.ShowBlog, tags=["Blogs"])
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
   
@app.get('/blogs/' ,  tags=["Blogs"])
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs  

@app.get('/blogs/{blog_id}', tags=["Blogs"])
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        return {"error": "Blog not found"}
    return blog


@app.delete('/blogs/{blog_id}', status_code=status.HTTP_204_NO_CONTENT ,tags=["Blogs"])
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        return {"error": "Blog not found"}
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

# @app.put('/blogs/{blog_id}', response_model=schemas.Blog , tags=["Blogs"])
# def update_blog(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
#     if not blog:
#         return {"error": "Blog not found"}
#     blog.title = request.title
#     blog.body = request.body
#     db.commit()
#     db.refresh(blog)
#     return blog



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post('/create-user/',response_model= schemas.ShowUser, tags=['Users'] ,status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    request.password = hashed_password
    new_user = models.User(username=request.username, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users/{user_id}',tags=['Users'], response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
           raise HTTPException(status_code=404, detail="User not found")

    return user





@app.get('/users/', tags=['Users'])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users






































if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")