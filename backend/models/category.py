# models/category.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)