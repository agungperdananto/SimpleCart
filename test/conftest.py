from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session


class ModelFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = Session()


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
