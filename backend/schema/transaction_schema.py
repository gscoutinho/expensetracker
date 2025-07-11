# handlers/transaction_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    occurred_at: datetime
    currency_id: int
    card_type_id: int
    card_flag_id: int
    type_id: int
    status_id: int
    category_id: int
    user_id: int

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    amount: Optional[float]
    occurred_at: Optional[datetime]
    currency_id: Optional[int]
    card_type_id: Optional[int]
    card_flag_id: Optional[int]
    type_id: Optional[int]
    status_id: Optional[int]
    category_id: Optional[int]
    user_id: Optional[int]

class TransactionView(TransactionBase):
    id: int

class Config:
        orm_mode = True