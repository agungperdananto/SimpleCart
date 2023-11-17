import factory
import json
import random
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session
from engine import base_engine as engine
from flask import jsonify

from api.models import Product

session = Session(engine)

class ModelFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = Session()


class FactoryProduct(ModelFactory):
    sku = factory.Faker('text')
    brand = factory.Faker('name')
    name = factory.Faker('name')
    description = factory.Faker('sentence')
    price = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    non_discountable = factory.Faker('boolean')

    class Meta:
        model = Product

def test_product_api(client):
    response = client.get("/api/products")
    print('Response', json.loads(response.data))
    assert response.status_code == 200

def test_product():
    product = FactoryProduct(id=2)
    assert product.price is not None


def test_product_detail_api(client):
    id = 1
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')

def create_factory():
    product = FactoryProduct(id=1)
    data = Product(
        sku = product.sku,
        brand = product.brand,
        name = product.name,
        description = product.description,
        price = product.price,
        non_discountable = product.non_discountable)
    session.add(data)
    session.commit()

# from api.models import Product, Cart

# from factory.alchemy import SQLAlchemyModelFactory
# from unittest.mock import MagicMock, patch

# def test_product(mocked_session):
#     product = mocked_session.query(Product).filter_by(id=1).first()
#     assert product.brand == "Indofood"

# def test_cart(mocked_session):
#     cart = mocked_session.query(Cart).filter_by(id=1).first()
#     assert cart.grand_total == (cart.shipping_fee + cart.subtotal)