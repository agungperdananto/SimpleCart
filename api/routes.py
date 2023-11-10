from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from .models import Product
from engine import base_engine as engine

home_api = Blueprint('api', __name__)

session = Session(engine)


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
        """
    keyword = request.args.get('q')
    sku = request.args.get('sku')

    query = select(Product)

    if keyword:
       query = query.where(Product.name.ilike(f'%{keyword}%'))
    
    if sku:
        sku_list = sku.split(',')
        query = query.where(Product.sku.in_(sku_list))

    result = [
        {   
            'id': product.id,
            'sku': product.sku,
            'brand': product.brand, 
            'name': product.name,
            'description': product.description, 
            'price': product.price,
            'non_discountable': product.non_discountable
            } 
            for product in session.scalars(query)
    ]

    return jsonify(result), 200


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
        """

    query = select(Product).where(Product.id == id)
    try:
        result =  session.scalars(query).one()
    except NoResultFound:
        return 'product not found', 404

    return {
         'id': result.id,
            'sku': result.sku,
            'brand': result.brand, 
            'name': result.name,
            'description': result.description, 
            'price': result.price,
            'non_discountable': result.non_discountable
    }, 200


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
        """
    return {}, 200

