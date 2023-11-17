import pytest

from app import create_app
from .test_models import create_factory


create_factory()


@pytest.fixture
def app():
    # mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    # mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    # mocker.patch("api.routes.products", return_value=[])
    # mocker.patch("api.routes.product_detail", return_value={"id": 1})
    app = create_app()
    return app

   

# import pytest

# from api.models import Base

# @pytest.fixture(scope="function")
# def sqlalchemy_declarative_base():
#     return Base

# @pytest.fixture(scope="function")
# def sqlalchemy_mock_config():
#     return [("product", [
#         {
#             "id": 1,
#             "sku":"INDO123",
#             "brand": "Indofood", 
#             "name":"test product name",
#             "description": "test product description",
#             "price": 1000,
#             "non_discountable": False
#         }
#     ]),
#     ("cart", [
#         {
#             "id": 1,
#             "coupon_code": "",
#             "shipping_fee": 1000,
#             "subtotal": 1000,
#             "grand_total": 2000
#         }
#     ])
#     ]
