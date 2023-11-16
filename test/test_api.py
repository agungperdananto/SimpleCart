import sys
from api.models import Product

def data_validation(data):
    '''
    format data = {
    'id': 1
    }
    '''
    data_keys = data.keys()
    return 'id' in data_keys

# def test_negative():
#     assert 3 != 5

# def test_positive():
#     assert 10 > 4

def test_data_validation():
    valid_data = {'id': 1, 'name': 'rudi'}
    valid_result = True 
    invalid_data = {'name': 'rudi', 'place': 'jakarta'}
    invalid_result = False
    assert data_validation(valid_data) == valid_result 
    assert data_validation(invalid_data) == invalid_result