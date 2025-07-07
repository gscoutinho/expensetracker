"""Back-end currencies model for the expense tracker system"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Union, Optional, List, Any
from decimal import Decimal, getcontext
from datetime import datetime
from .users import User

class CurrByCountry(Enum):
    """Dedicated class for countries' currency. This will be updated in the future the query from web."""
    BRASIL = "BRL"
    CANADA = "CAD"
    USA = "USD"

class CardType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

class CardFlag(Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"

@dataclass
class MoneyBase:
    v : Decimal = field(
        default_factory= lambda: Decimal("0.00"), metadata={"description":"Amount in decimal"}
    )
    t: datetime
    c: CurrByCountry = CurrByCountry.CANADA

    def __post_init__(self):
        #ensure that if someone passes a float or str, it becomes a Decimal
        if not  isinstance(self.v, Decimal):
            self.v = Decimal(str(self.v)).quantize(Decimal("0.00"))


@dataclass
class Money(MoneyBase):
    """Dedicated class for money currency."""

@dataclass
class CreditPurchase(MoneyBase):
    """Dedicated class for credit purchase."""
    id : str
    description : str
    purchased_at : str
    installments : Optional[int] = 0
    current_installment : Optional[int] = 0

@dataclass
class CreditCard:
    """Dedicated class for credit cards."""
    name : str
    bank : str
    flag : CardFlag = CardFlag.VISA
    v_limit : Decimal
    balance : Decimal
    records : List[CreditPurchase] = None


@dataclass
class Account:
    acc_number : str
    bank : str
    owner : User
    balance: Decimal
    credit_cards: Optional[List[CreditCard]] = None