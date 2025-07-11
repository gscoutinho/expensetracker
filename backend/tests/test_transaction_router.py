# tests/test_transaction_router.py
from datetime import datetime

def test_transaction_endpoints(test_client):
    # create dependencies
    user_resp = test_client.post("/users/", json={"username": "tu", "email": "tu@example.com"})
    uid = user_resp.json()["id"]
    cat_resp = test_client.post("/categories/", json={"name": "Tcat", "description": null})
    cid = cat_resp.json()["id"]

    payload = {
        "amount": 5.0,
        "occurred_at": datetime.utcnow().isoformat(),
        "currency_id": 1,
        "card_type_id": 1,
        "card_flag_id": 1,
        "type_id": 1,
        "status_id": 1,
        "category_id": cid,
        "user_id": uid
    }
    r = test_client.post("/transactions/", json=payload)
    assert r.status_code == 200
    tid = r.json()["id"]

    r2 = test_client.get(f"/transactions/{tid}")
    assert r2.status_code == 200

    r3 = test_client.put(f"/transactions/{tid}", json={"amount": 7.5})
    assert float(r3.json()["amount"]) == 7.5

    r4 = test_client.delete(f"/transactions/{tid}")
    assert r4.status_code == 200