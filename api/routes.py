from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from

home_api = Blueprint('api', __name__)


@home_api.route('/products', methods=["GET"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'product list'
        }
    }
})
def products():
    """
        Product list
        ---
        parameters:
          - in: query
            name: q
            type: string
            required: false
          - in: query
            name: sku
            type: string
            required: false
        responses:
          200:
            description: list of products
        """
    keyword = request.args.get('q')
    sku = request.args.get('sku')

    print(f'keyword: {keyword}')
    print(f'sku: {sku}')

    result = [
        {'id': 1, 
         'name': 'product 1'
         },
        {'id': 2, 
         'name': 'product 2'
         }
    ]

    return result, 200


@home_api.route('/products/<id>', methods=["GET"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'product detail'
        }
    }
})
def product_detail(id):
    """
        Product Detail
        ---
        parameters:
          - in: path
            name: id
            type: string
            required: true
        responses:
          200:
            description: product detail
        """
    print('ID', id)

    result =  {'id': 1,
         'name': 'product 1'
         }

    return result, 200


@home_api.route('/cart', methods=["GET", "POST"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'cart list'
        }
    }
})
def active_carts():
    """
        list of active cart
        ---
        post:
            parameters:
              - in: body
                name: cart
                type: object
                required:
                    - cart_items
                properties:
                    coupon_code:
                        type: string
                    cart_items:
                        type: array
                        items:
                            type: object
                            required:
                                - product_id
                                - qty
                            properties:
                                product_id: 
                                    type: integer
                                qty: 
                                    type: integer
        responses:
          200:
            description: cart detail
        """
    return [], 200


@home_api.route('/cart/<id>', methods=["GET", "PUT", "DELETE"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'cart'
        }
    }
})
def cart(id):
    """
        cart detail
        ---
        get:
            parameters:
              - in: query
                name: set_promo
                type: string
                required: false
                default: 1
        put:
            parameters:
              - in: body
                name: cart
                type: object
                required:
                    - cart_items
                properties:
                    coupon_code:
                        type: string
                    cart_items:
                        type: array
                        items:
                            type: object
                            required:
                                - product_id
                                - qty
                            properties:
                                product_id: 
                                    type: integer
                                qty: 
                                    type: integer
        
        responses:
          200:
            description: cart detail
        """
    return {}, 200

