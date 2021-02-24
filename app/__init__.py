from flask_restx import Api
from flask import Blueprint

# Namespaces
from .main.controller.product_controller import api as prod_ns
from .main.controller.store_controller import api as store_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Cargamos Store API',
          version='1',
          prefix='/api/v1',
          description='API REST'
          )

api.add_namespace(prod_ns, path='/products')
api.add_namespace(store_ns, path='/stores')