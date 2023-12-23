import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

# post new cart
def test_post_cart(client):
    response = client.post("/api/cart", json={
        "coupon_code": "",
        "shipping_fee": 30000,
        "cart_items": [{
            "product_id": 5,
            "qty": 2
        }]
    })
    assert response.status_code == 200
    assert b"data created" in response.data
