""" Operations needed for the endpoints of the resource: products"""

# DB
from app.main import db
# Models
from app.main.model.models import Product
#Utils
from .utils import save_changes, success

def save_new_product(data):
    """ Add new product"""
    product = Product.query.filter_by(product_name=data['product_name']).first()
    if not product:
        new_product = Product(   # **data
            product_name=data['product_name'],
            description=data['description'],
            list_price=data['list_price']
        )
        save_changes(new_product)
        return success(new_product)

    response_object = {
        'status': 'Fail',
        'messsage': 'Product already exits.'
    }
    return response_object, 409
    

def  get_all_products():
    return Product.query.all()


# def get_a_product(product_sku):
#     return Product.query.filter_by(sku=product_sku).first()
