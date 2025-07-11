# service/category_service.py
from sqlalchemy.orm import Session
from models.category import Category


def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, data: dict):
    cat = Category(**data)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def update_category(db: Session, category_id: int, updates: dict):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if not cat:
        return None
    for key, value in updates.items():
        setattr(cat, key, value)
    db.commit()
    db.refresh(cat)
    return cat

def delete_category(db: Session, category_id: int):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if cat:
        db.delete(cat)
        db.commit()
    return cat