import unittest

from app.main import db
import json
from app.test.base import BaseTestCase
from app.main.model.models import Product
from flask_restx import fields, Model

from collections import OrderedDict


def product_creation(self):
    return self.client.post(
        '/api/v1/products/',
        data=json.dumps(dict(
            sku=100,
            product_name='This is a name',
            description="This is a description",
            list_price=100
        )),
        content_type='application/json'
    )


class TestProductModel(BaseTestCase):

    def test_model_as_flat_dict(self):
        model = Model('Store', {
            'product_name': fields.String,
            'description': fields.String,
            'list_price': fields.Float
        })
        self.assertIsInstance(model, dict)
        self.assertNotIsInstance(model, OrderedDict)

    def test_registration(self):
        with self.client:
            response = product_creation(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] , "Sucess")
            self.assertTrue(data['message'], 'Resource successfully added.')
            self.assertTrue(data['sku'], 100)
            self.assertTrue(data['product_name'], 'This is a name')
            self.assertTrue(data['description'], 'This is a description')
            self.assertTrue(data['list_price'], 100)
            self.assertTrue(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 201)
