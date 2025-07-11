# tests/test_category_router.py

def test_category_endpoints(test_client):
    payload = {"name": "APIcat", "description": "Via API"}
    r = test_client.post("/categories/", json=payload)
    assert r.status_code == 200
    cat_id = r.json()["id"]

    r2 = test_client.get(f"/categories/{cat_id}")
    assert r2.status_code == 200

    r3 = test_client.put(f"/categories/{cat_id}", json={"description": "Updated"})
    assert r3.json()["description"] == "Updated"

    r4 = test_client.delete(f"/categories/{cat_id}")
    assert r4.status_code == 200