import json

def test_product_detail_api(client):
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

