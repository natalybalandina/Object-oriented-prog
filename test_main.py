from main import Product, Category
import pytest

class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        Category.total_categories += 1

# Тесты
import pytest

class TestProduct:
    def test_product_creation(self):
        product = Product("Test Product", "This is a test product", 10.99, 100)
        assert product.name == "Test Product"
        assert product.description == "This is a test product"
        assert product.price == 10.99
        assert product.quantity == 100

    def test_get_total_products(self):
        Product.total_products = 0
        product1 = Product("Product 1", "Description 1", 5.99, 10)
        product2 = Product("Product 2", "Description 2", 15.99, 20)
        assert Product.total_products == 2

class TestCategory:
    def test_category_creation(self):
        category = Category("Test Category", "This is a test category")
        assert category.name == "Test Category"
        assert category.description == "This is a test category"

    def test_get_total_categories(self):
        Category.total_categories = 0
        category1 = Category("Category 1", "Description 1")
        category2 = Category("Category 2", "Description 2")
        assert Category.total_categories == 2

if __name__ == "__main__":
    pytest.main()
