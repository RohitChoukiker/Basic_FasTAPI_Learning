from database import Base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), )
    creator = relationship("User", back_populates="blogs")
    
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)  # In a real application, ensure to hash passwords    
    
    blogs = relationship("Blog", back_populates="creator")