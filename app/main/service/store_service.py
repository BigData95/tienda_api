
""" Operations needed for the endpoints of the resource: stores"""

# DB
from app.main import db
# Models
from app.main.model.models import Store, Stock, Product
# Utils
from .utils import save_changes, success

# Saves


def save_new_store(data):
    """ Add new store to the database """
    store = Store.query.filter_by(store_name=data['store_name']).first()
    if not store:
        new_store = Store(  # **data
            store_name=data['store_name'],
            phone=data['phone'],
            email=data['email'],
            street=data['street'],
            city=data['city'],
            state=data['state']
        )
        save_changes(new_store)
        return success(new_store)

    response_object = {
        'status': 'Fail',
        'messsage': 'Store already exits.'
    }
    return response_object, 409


def save_new_store_product(data, name):
    """ Add/Associate product to store"""

    stock = Stock.query.filter_by(
        store_name=name, product_name=data['product_name']).first()
    if stock:
        response_object = {
            'status': 'Fail',
            'messsage': 'Product already has stock defined in the store'
        }
        return response_object, 409

    store = Store.query.filter_by(store_name=name).first()
    if not store:
        response_object = {
            'status': 'Fail',
            'messsage': 'Store does not exist.'
        }
        return response_object, 409

    product = Product.query.filter_by(
        product_name=data['product_name']).first()
    if not product:
        product = Product(
            product_name=data['product_name'],
            description=data['description'],
            list_price=data['list_price']
        )
        save_changes(product)

    new_stock = Stock(
        store_name=store.store_name,
        product_name=product.product_name,
        quantity=data['quantity']
    )
    save_changes(new_stock)

    response_info = {
        'status': 'Success',
        'message': 'Resource successfully added.',
        'store': store.store_name,
        'product': product.product_name,
        'description': product.description,
        'list_price': product.list_price,
        'quantity': new_stock.quantity
    }
    return response_info, 201


# Gets


def get_all_stores():
    """Retrive all stores in the database """
    return Store.query.all()


def user_search_product(store_name, product_name, search_term):
    """ Specific query, return null if false """
    # Lucky for us, stock can have just 1 more search term 
    stock = Stock.query.filter_by(store_name=store_name,
                                  product_name=product_name
                                  ).first()
    print(stock)
    if not stock:
        response_object = {
            'status': 'Fail',
            'messsage': 'Stock does not exist'
        }
        return response_object, 409
    print(stock.quantity)
    print(search_term)
    if int(stock.quantity) >= int(search_term):
        return {"Result": "Suficiente stock"}
    return {"Result": "Insuficiente stock"}


# def get_datail_product(store_name, product_name):
#     """ Get detail on a specific product on a specific store """
#     return Stock.query.filter_by(
#         store_name=store_name, product_name=product_name).first()

# def get_store_products():
#     """ List of all products in the store """
#     pass
