""" Dto's for all models and their relations """


from flask_restx import Namespace, fields


class UserDto:
    """ User model Dto """
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ProductDto:
    """ Product and stock model Dto """
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        # 'product_sku': fields.Integer(required=True, description='Product Sku'),
        'product_name': fields.String(description='Product name'),
        'description': fields.String(description='Product description'),
        'list_price': fields.Integer(description='Product price')
    })

    stock = api.inherit('stock', product, {
        'quantity': fields.Integer(required=True, description='Quantity of products available')
    })


class StoreDto:
    """ Store model Dto """
    api = Namespace('store', description='store related operations')
    store = api.model('store', {
        # 'store_id': fields.Integer(required=True, description='Store unique identifier'),
        'store_name': fields.String(required=True, description='Store name'),
        'phone': fields.String(description='Store phone'),
        'email': fields.String(description='Store email'),
        'street': fields.String(description='Adress: street'),
        'city': fields.String(description='Adress: city'),
        'state': fields.String(description='Adress: state')
    })
