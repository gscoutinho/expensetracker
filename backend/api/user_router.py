from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from handlers.user_handler import (
    list_users, retrieve_user, create_user_handler,
    update_user_handler, delete_user_handler, UserCreate, UserUpdate, UserView
)
from models.base import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserView])
def get_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)

@router.get("/{user_id}", response_model=UserView)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return retrieve_user(user_id, db)

@router.post("/", response_model=UserView)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_handler(user, db)

@router.put("/{user_id}", response_model=UserView)
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user_handler(user_id, user, db)

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return delete_user_handler(user_id, db)