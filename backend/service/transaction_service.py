# service/transaction_service.py
from sqlalchemy.orm import Session
from models.transaction import Transaction

def get_transactions(db: Session):
    return db.query(Transaction).all()

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def create_transaction(db: Session, data: dict):
    tx = Transaction(**data)
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def update_transaction(db: Session, transaction_id: int, updates: dict):
    tx = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not tx:
        return None
    for key, value in updates.items():
        setattr(tx, key, value)
    db.commit()
    db.refresh(tx)
    return tx

def delete_transaction(db: Session, transaction_id: int):
    tx = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if tx:
        db.delete(tx)
        db.commit()
    return tx