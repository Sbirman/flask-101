# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_products_id_valid(self):
        response = self.client.get("/api/v1/products/2")
        products = response.json
        self.assertIsInstance(products, dict)

    def test_products_id_fail(self):
        response = self.client.get("/api/v1/products/6")
        self.assertTrue(response.status_code == 404)
