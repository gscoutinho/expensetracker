# models/transaction.py
from sqlalchemy import Column, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(14, 2), nullable=False)
    occurred_at = Column(DateTime(timezone=True), nullable=False)
    currency_id = Column(Integer, ForeignKey("currency.id"), nullable=False)
    card_type_id = Column(Integer, ForeignKey("card_type.id"), nullable=False)
    card_flag_id = Column(Integer, ForeignKey("card_flag.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("transaction_type.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("transaction_status.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False, default=1)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    category = relationship("Category")
    user = relationship("User")
    credit_purchase = relationship("CreditPurchase", uselist=False, back_populates="transaction")