import requests

class Database:
    def save_product(self, product):
        # Simulate an API call to save product
        response = requests.post("https://example.com/api/save", json=product.to_dict())
        return response.status_code == 200
