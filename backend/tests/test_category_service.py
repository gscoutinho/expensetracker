# tests/test_category_service.py
from service.category_service import create_category, get_category, update_category, delete_category, get_categories

def test_category_crud(db_session):
    data = {"name": "TestCat", "description": "Desc"}
    cat = create_category(db_session, data)
    assert cat.id
    assert cat.name == "TestCat"

    fetched = get_category(db_session, cat.id)
    assert fetched.description == "Desc"
    assert len(get_categories(db_session)) == 1

    updated = update_category(db_session, cat.id, {"name": "UpdatedCat"})
    assert updated.name == "UpdatedCat"

    deleted = delete_category(db_session, cat.id)
    assert deleted.id == cat.id
    assert get_category(db_session, cat.id) is None