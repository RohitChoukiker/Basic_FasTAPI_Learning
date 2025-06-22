from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import models
import schemas
from repository import userRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)

@router.post('/create-user/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(request, db)

@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return userRepository.get_by_id(user_id, db)

@router.get('/', response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return userRepository.get_all(db)

@router.put('/{user_id}', response_model=schemas.ShowUser)
def update_user(user_id: int, request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.update(user_id, request, db)

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return userRepository.delete(user_id, db)

@router.get('/username/{username}', response_model=schemas.ShowUser)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return userRepository.get_by_username(username, db)