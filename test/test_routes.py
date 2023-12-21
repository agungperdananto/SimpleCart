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
    
def test_post_cart(client):
    # Define a sample data payload for creating a new cart
    cart_data = {
        "coupon_code": "DISCOUNT123",
        "shipping_fee": 5.0,
        "cart_items": [
            {"product_id": 1, "qty": 2},
            {"product_id": 3, "qty": 1}
        ]
    }

    # Make a POST request to create a new cart
    response = client.post("/api/cart", json=cart_data)
    
    # Check that the response status code is 200 (OK)
    assert response.status_code ==200
