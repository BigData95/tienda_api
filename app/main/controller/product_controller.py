
from flask import request
from flask_restx import Resource 

from ..util.dto import ProductDto
from ..service.product_service import get_all_products, save_new_product

from typing import Dict, Tuple

api = ProductDto.api
_products = ProductDto.product


@api.route('/')
class ProductList(Resource):
    @api.doc('List of all avaliable products')
    @api.marshal_list_with(_products, envelope='data')
    def get(self):
        """List all products"""
        return get_all_products()

    @api.expect(_products, validate=True)
    @api.response(201, 'Store successfully created.')
    @api.doc('create new product with no store association')
    def post(self):
        """ "B: Una entidad Producto que almacene la informacion asociada a la misma" """
        data = request.json
        return save_new_product(data=data)
