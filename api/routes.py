from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from

home_api = Blueprint('api', __name__)


@home_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit'
        }
    }
})
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = {
        "messages": "hello world"
    }
    return result, 200
