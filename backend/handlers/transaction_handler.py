from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schema.transaction_schema import TransactionCreate, TransactionUpdate, TransactionView
from service.transaction_service import (
    get_transactions, get_transaction,
    create_transaction, update_transaction,
    delete_transaction
)
from models.base import get_db

def list_transactions(db: Session = Depends(get_db)):
    return get_transactions(db)

def retrieve_transaction(transaction_id: int, db: Session = Depends(get_db)):
    tx = get_transaction(db, transaction_id)
    if not tx:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return tx

def create_transaction_handler(tx: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, tx.dict())

def update_transaction_handler(transaction_id: int, tx: TransactionUpdate, db: Session = Depends(get_db)):
    updated = update_transaction(db, transaction_id, tx.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return updated

def delete_transaction_handler(transaction_id: int, db: Session = Depends(get_db)):
    deleted = delete_transaction(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return {"ok": True}