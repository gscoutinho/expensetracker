# tests/test_user_router.py
import json

def test_user_endpoints(test_client):
    # Create
    payload = {"username": "ruser", "email": "r@example.com"}
    r = test_client.post("/users/", json=payload)
    assert r.status_code == 200
    data = r.json()
    user_id = data["id"] if isinstance(data, list) else data.get("id")
    assert data["username"] == "ruser"

    # Read
    r2 = test_client.get(f"/users/{user_id}")
    assert r2.status_code == 200
    # Update
    r3 = test_client.put(f"/users/{user_id}", json={"email": "rr@example.com"})
    assert r3.status_code == 200
    assert r3.json()["email"] == "rr@example.com"

    # Delete
    r4 = test_client.delete(f"/users/{user_id}")
    assert r4.status_code == 200