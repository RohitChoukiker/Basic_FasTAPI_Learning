from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True
        
        
class ShowBlog(BlogBase):
    id: int
    user_id: int
    creator: Optional['ShowUser'] = None  # Optional creator details

    class Config():
        orm_mode = True     
     
     
     
     
        
class UserBase(BaseModel):
    username: str
    email: str
    password: str   
      
    
class User(UserBase):
    
    
    class Config():
        orm_mode = True    
        
        
class ShowUser(BaseModel):
    username: str
    email: str     
    
    class Config():
        orm_mode = True   