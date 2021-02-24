import unittest

from app.main import db
import json
from app.test.base import BaseTestCase
from app.main.model.models import Store
from flask_restx import fields, Model

from collections import OrderedDict


def store_creation(self):
    return self.client.post(
        '/api/v1/stores/',
        data=json.dumps(dict(
            store_id=100,
            store_name='This is a name',
            phone='5533412221',
            email='correo@correo.com',
            street='street',
            city='city',
            state='state'
        )),
        content_type='application/json'
    )


class TestStoreModel(BaseTestCase):

    def test_model_as_flat_dict(self):
        model = Model('Store', {
            'store_name': fields.String,
            'phone': fields.String,
            'email': fields.String,
            'street': fields.String,
            'city': fields.String,
            'state': fields.String
        })
        self.assertIsInstance(model, dict)
        self.assertNotIsInstance(model, OrderedDict)

    def test_store_creation(self):
        with self.client:
            response = store_creation(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'], "Sucess")
            self.assertTrue(data['message'], 'Resource successfully added.')
            self.assertTrue(data['store_id'], 100)
            self.assertTrue(data['store_name'], 'This is a name')
            self.assertTrue(data['phone'], '5533412221')
            self.assertTrue(data['email'], 'correo@correo.com')
            self.assertTrue(data['street'], 'street')
            self.assertTrue(data['city'], 'city')
            self.assertTrue(data['state'], 'state')
            self.assertTrue(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 201)
