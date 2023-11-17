import factory
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.orm import Session
from engine import base_engine as engine

from .settings import DEFAULT_PRICE


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
    price = DEFAULT_PRICE
    non_discountable = factory.Faker('boolean')

    class Meta:
        model = Product


def test_product():
    product = FactoryProduct(id=2)
    assert product.price is not None


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