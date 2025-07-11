# tests/test_transaction_service.py
from datetime import datetime
from service.transaction_service import create_transaction, get_transaction, update_transaction, delete_transaction, get_transactions

from service.user_service import create_user
from service.category_service import create_category

import pytest

@pytest.fixture
def tx_data(db_session):
    user = create_user(db_session, {"username": "u1", "email": "u1@example.com"})
    cat = create_category(db_session, {"name": "Cat1", "description": None})
    return {
        "amount": 10.5,
        "occurred_at": datetime.utcnow(),
        "currency_id": 1,
        "card_type_id": 1,
        "card_flag_id": 1,
        "type_id": 1,
        "status_id": 1,
        "category_id": cat.id,
        "user_id": user.id,
    }

def test_transaction_crud(db_session, tx_data):
    tx = create_transaction(db_session, tx_data)
    assert tx.id

    fetched = get_transaction(db_session, tx.id)
    assert fetched.amount == tx_data["amount"]
    assert len(get_transactions(db_session)) == 1

    updated = update_transaction(db_session, tx.id, {"amount": 20.0})
    assert float(updated.amount) == 20.0

    deleted = delete_transaction(db_session, tx.id)
    assert deleted.id == tx.id
    assert get_transaction(db_session, tx.id) is None