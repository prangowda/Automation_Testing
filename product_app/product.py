class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)
        return product

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def delete_product(self, name):
        product = self.get_product(name)
        if product:
            self.products.remove(product)
            return True
        return False
