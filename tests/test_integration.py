import unittest
from unittest.mock import patch
from product_app.product import ProductManager
from product_app.database import Database

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.manager = ProductManager()

    @patch('product_app.database.requests.post')
    def test_save_product_to_database(self, mock_post):
        # Simulate a successful API call
        mock_post.return_value.status_code = 200

        db = Database()
        product = self.manager.add_product("Phone", 800)
        result = db.save_product(product)

        mock_post.assert_called_once()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
