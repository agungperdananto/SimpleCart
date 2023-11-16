import factory
import random
from .conftest import ModelFactory

from api.models import Product

class FactoryProduct(ModelFactory):
    sku = factory.Faker('text')
    brand = factory.Faker('name')
    name = factory.Faker('name')
    description = factory.Faker('sentence')
    price = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    non_discountable = factory.Faker('boolean')

    class Meta:
        model = Product


def test_product():
    product = FactoryProduct(id=2)
    assert product.price is not None


# from api.models import Product, Cart

# from factory.alchemy import SQLAlchemyModelFactory
# from unittest.mock import MagicMock, patch

# def test_product(mocked_session):
#     product = mocked_session.query(Product).filter_by(id=1).first()
#     assert product.brand == "Indofood"

# def test_cart(mocked_session):
#     cart = mocked_session.query(Cart).filter_by(id=1).first()
#     assert cart.grand_total == (cart.shipping_fee + cart.subtotal)