import json

def test_product_detail_api(client):
    # Test retrieving details of an existing product
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')

    # Test retrieving details of another existing product
    another_id = 2
    response = client.get(f"/api/products/{another_id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert another_id == data.get('id')

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

    # Test retrieving the list of products with an invalid search keyword
    invalid_keyword = "!@#$%^"
    response = client.get(f"/api/products?q={invalid_keyword}")
    assert response.status_code == 200  # Depending on the expected behavior
    data = json.loads(response.data)
    assert len(data) == 0  # Assuming an invalid keyword returns an empty list

    # Test retrieving the list of products with multiple SKUs
    sku_list = "sku1,sku2,sku3"
    response = client.get(f"/api/products?sku={sku_list}")
    assert response.status_code == 200

def test_cart_api(client):
    # Test retrieving the list of active carts
    response = client.get("/api/cart")
    assert response.status_code == 200

    # Test creating a new cart with valid data
    cart_data = {
        "coupon_code": "DISCOUNT",
        "shipping_fee": 10.0,
        "cart_items": [{"product_id": 1, "qty": 2}]
    }
    response = client.post("/api/cart", json=cart_data)
    assert response.status_code == 200

    # Test creating a new cart with invalid data
    invalid_cart_data = {
        "coupon_code": "INVALID_CODE",
        "shipping_fee": "not_a_number",  # Invalid data type
        "cart_items": [{"product_id": 1, "qty": -1}]  # Invalid quantity
    }
    response = client.post("/api/cart", json=invalid_cart_data)
    assert response.status_code == 400  # Depending on the expected behavior
