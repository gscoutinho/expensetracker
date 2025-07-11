from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base

class CreditPurchase(Base):
    __tablename__ = "credit_purchases"
    transaction_id = Column(Integer, ForeignKey("transactions.id", ondelete="CASCADE"), primary_key=True)
    credit_details = Column(JSON, nullable=True)

    transaction = relationship("Transaction", back_populates="credit_purchase")