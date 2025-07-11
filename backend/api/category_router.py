# api/category_router.py
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from handlers.category_handler import (
    list_categories,
    retrieve_category,
    create_category_handler,
    update_category_handler,
    delete_category_handler
)
from schema.category_schema import CategoryCreate, CategoryUpdate, CategoryView
from models.base import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryView])
def get_categories_endpoint(db: Session = Depends(get_db)):
    return list_categories(db)

@router.get("/{category_id}", response_model=CategoryView)
def get_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    return retrieve_category(category_id, db)

@router.post("/", response_model=CategoryView)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category_handler(category, db)

@router.put("/{category_id}", response_model=CategoryView)
def update_category_endpoint(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return update_category_handler(category_id, category, db)

@router.delete("/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    return delete_category_handler(category_id, db)