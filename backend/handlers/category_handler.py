# handlers/category_handler.py
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schema.category_schema import CategoryCreate, CategoryUpdate, CategoryView
from service.category_service import (
    get_categories, get_category, create_category,
    update_category, delete_category
)
from models.base import get_db

def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)

def retrieve_category(category_id: int, db: Session = Depends(get_db)):
    cat = get_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return cat

def create_category_handler(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category.dict())

def update_category_handler(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated = update_category(db, category_id, category.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return updated

def delete_category_handler(category_id: int, db: Session = Depends(get_db)):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return {"ok": True}