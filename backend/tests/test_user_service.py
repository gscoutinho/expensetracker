# tests/test_user_service.py
import pytest
from service.user_service import create_user, get_user, update_user, delete_user, get_users
from schema.user_schema import UserCreate

def test_user_crud(db_session):
    # Create
    user_data = {"username": "testuser", "email": "test@example.com"}
    user = create_user(db_session, user_data)
    assert user.id is not None
    assert user.username == "testuser"

    # Read
    fetched = get_user(db_session, user.id)
    assert fetched.email == "test@example.com"
    assert len(get_users(db_session)) == 1

    # Update
    updated = update_user(db_session, user.id, {"email": "new@example.com"})
    assert updated.email == "new@example.com"

    # Delete
    deleted = delete_user(db_session, user.id)
    assert deleted.id == user.id
    assert get_user(db_session, user.id) is None