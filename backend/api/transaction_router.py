# api/transaction_router.py
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from handlers.transaction_handler import (
    list_transactions,
    retrieve_transaction,
    create_transaction_handler,
    update_transaction_handler,
    delete_transaction_handler
)
from schema.transaction_schema import TransactionCreate, TransactionUpdate, TransactionView
from models.base import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/", response_model=List[TransactionView])
def get_transactions_endpoint(db: Session = Depends(get_db)):
    return list_transactions(db)

@router.get("/{transaction_id}", response_model=TransactionView)
def get_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    return retrieve_transaction(transaction_id, db)

@router.post("/", response_model=TransactionView)
def create_transaction_endpoint(tx: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction_handler(tx, db)

@router.put("/{transaction_id}", response_model=TransactionView)
def update_transaction_endpoint(transaction_id: int, tx: TransactionUpdate, db: Session = Depends(get_db)):
    return update_transaction_handler(transaction_id, tx, db)

@router.delete("/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    return delete_transaction_handler(transaction_id, db)