# def test_example(client):
#     response = client.get("/api/products/1")
#     print('Response', response)
#     assert response.status_code == 200

# from flask import session

# def test_access_session(app):
#     c = app.test_client()
#     response = c.get('/api/products/1')

# from unittest.mock import MagicMock, patch

# from api.routes import products

# def test_LegendsPostService_can_init():
#     session = MagicMock()
#     service = products(_session=session)
#     assert service.session is session