from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]

class UserView(UserBase):
    id: int
    created_at: datetime

class Config:
        orm_mode = True