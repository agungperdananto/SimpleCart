from api.utils import get_price, get_subtotal
from api.models import Product

from .settings import DEFAULT_PRICE


def test_get_price():
    product_ids = []
    for index in range(2):
        id = index + 1
        product = Product(id=id)
        product_ids.append(product.id)
    prices = {id: id * DEFAULT_PRICE for id in product_ids}
    assert prices == get_price(product_ids)


def test_get_subtotal():
    product_id_1 = 1
    product_id_2 = 2
    qty_1 = 3
    qty_2 = 2
    cart = {
        'cart_items': [
            {
                'product_id': product_id_1,
                'qty': qty_1
            },
            {
                'product_id': product_id_2,
                'qty': qty_2
            },
        ]
    }
    assert sum([DEFAULT_PRICE * product_id_1 * qty_1, DEFAULT_PRICE * product_id_2 * qty_2]) == get_subtotal(cart)['subtotal']
