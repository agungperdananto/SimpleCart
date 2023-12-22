import json

def test_product_detail_api(client):
    # Test retrieving details of an existing product
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')

    # Test retrieving details of a non-existent product
    non_existent_id = 999
    response = client.get(f"/api/products/{non_existent_id}")
    assert response.status_code == 404

def test_product_api(client):
    # Test retrieving the list of products without any filters
    response = client.get("/api/products")
    assert response.status_code == 200

    # Test retrieving the list of products with a search keyword
    keyword = "example"
    response = client.get(f"/api/products?q={keyword}")
    assert response.status_code == 200

    # Test retrieving the list of products with multiple SKUs
    sku_list = "sku1,sku2,sku3"
    response = client.get(f"/api/products?sku={sku_list}")
    assert response.status_code == 200

def test_cart_api(client):
    # Test retrieving the list of active carts
    response = client.get("/api/cart")
    assert response.status_code == 200

    # Test creating a new cart
    cart_data = {
        "coupon_code": "DISCOUNT",
        "shipping_fee": 10.0,
        "cart_items": [{"product_id": 1, "qty": 2}]
    }
    response = client.post("/api/cart", json=cart_data)
    assert response.status_code == 200

    