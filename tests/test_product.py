import unittest
from product_app.product import ProductManager

class TestProductManager(unittest.TestCase):
    def setUp(self):
        self.manager = ProductManager()

    def test_add_product(self):
        product = self.manager.add_product("Laptop", 1200)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1200)

    def test_get_product(self):
        self.manager.add_product("Laptop", 1200)
        product = self.manager.get_product("Laptop")
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Laptop")

    def test_delete_product(self):
        self.manager.add_product("Laptop", 1200)
        result = self.manager.delete_product("Laptop")
        self.assertTrue(result)
        self.assertIsNone(self.manager.get_product("Laptop"))

if __name__ == '__main__':
    unittest.main()
