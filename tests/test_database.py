import unittest
from unittest.mock import patch
from product_app.database import Database
from product_app.product import Product

class TestDatabase(unittest.TestCase):
    @patch('product_app.database.requests.post')
    def test_save_product(self, mock_post):
        mock_post.return_value.status_code = 200

        product = Product("Tablet", 500)
        db = Database()
        result = db.save_product(product)

        mock_post.assert_called_once_with("https://example.com/api/save", json=product.to_dict())
        self.assertTrue(result)

    @patch('product_app.database.requests.post')
    def test_save_product_fail(self, mock_post):
        mock_post.return_value.status_code = 500

        product = Product("Tablet", 500)
        db = Database()
        result = db.save_product(product)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
