# handlers/user_handler.py
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schema.user_schema import UserCreate, UserUpdate, UserView
from service.user_service import (get_users, get_user, create_user, update_user, delete_user)
from models.base import get_db

def list_users(db: Session = Depends(get_db)):
    return get_users(db)

def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def create_user_handler(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.dict())

def update_user_handler(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated = update_user(db, user_id, user.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated

def delete_user_handler(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"ok": True}