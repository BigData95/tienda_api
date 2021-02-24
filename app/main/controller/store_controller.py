
from flask import request
from flask_restx import Resource
from ..util.dto import StoreDto, ProductDto
from ..service.store_service import (
    get_all_stores,
    save_new_store,
    save_new_store_product,
    user_search_product
)


# Dto's
api = StoreDto.api
_store = StoreDto.store
_product = ProductDto.product
_stock = ProductDto.stock


@api.route('/')
class StoreList(Resource):
    """" Base store URI """
    @api.doc('List of all avaliable products')
    @api.marshal_list_with(_store, envelope='data')
    def get(self):
        """List all stores"""
        return get_all_stores()

    @api.expect(_store, validate=True)
    @api.response(201, 'Store successfully created.')
    @api.doc('create new store')
    def post(self):
        """ "A: Una entidad tienda que almacene la informacion asociada a la misma" """
        data = request.json
        return save_new_store(data=data)


@api.route('/<string:name>/product')
@api.param('name', 'unique store name')
@api.response(404, 'Product not found in this store.')
class StoreProducts(Resource):
    # def get(self, name):
    #     """ Get detail of a product in a store """
    #     pass

    @api.expect(_stock, validate=True)
    @api.response(201, 'Product is now in the store.')
    @api.doc('Add/Associate product to store')
    def post(self, name):
        """ "C: Poder agregar/asociar inventario a una tienda" """
        data = request.json
        return save_new_store_product(data=data, name=name)


@api.route('/<string:store_name>/product/<product_name>/search/<search_term>')
@api.param('store_name', 'unique store name')
@api.param('product_name', 'unique product name')
@api.param('search_term', 'term use for seach')
@api.response(404, 'Resource not found')
class UserSearch(Resource):
    def get(self, store_name, product_name,  search_term):
        """ "D: Poder determinar si hay suficiente stock de un producto en la tienda" """
        return user_search_product(store_name, product_name, search_term)
