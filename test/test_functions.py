from api.utils import get_price
from .test_models import FactoryProduct

def test_get_price():
    product_ids = []
    prices = []
    for id in range(1):
        product = FactoryProduct(id=id + 1)
        prices.append(product.price)
        product_ids.append(product.id)
    assert prices == get_price(product_ids)
