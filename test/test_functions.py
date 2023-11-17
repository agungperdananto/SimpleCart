from api.utils import get_price, get_subtotal
from api.models import Product

from .settings import DEFAULT_PRICE


def test_get_price():
    prices = {1: DEFAULT_PRICE}
    product_ids = []
    for index in range(1):
        id = index + 1
        product = Product(id=id)
        product_ids.append(product.id)
    assert prices == get_price(product_ids)

def test_get_subtotal():
    product_id = 1
    qty = 3
    cart = {
        'cart_items': [
            {
                'product_id': product_id,
                'qty': qty
            }
        ]
    }
    assert DEFAULT_PRICE * qty == get_subtotal(cart)['subtotal']
