import pytest

from src.category import Category
from src.product import Product


class TestProduct:
    def test_product_creation(self):
        product = Product("Test Product", "This is a test product", 10.99, 100)
        assert product.name == "Test Product"
        assert product.description == "This is a test product"
        assert product.price == 10.99
        assert product.quantity == 100

    def test_get_total_products(self):
        Product.total_products = 0  # Сброс перед тестом
        product1 = Product("Product 1", "Description 1", 5.99, 10)
        product2 = Product("Product 2", "Description 2", 15.99, 20)

        # Проверяем общее количество продуктов
        assert Product.total_products == 2

        # Используем созданные продукты для проверки
        assert product1.name == "Product 1"
        assert product2.name == "Product 2"


class TestCategory:
    def test_category_creation(self):
        category = Category("Test Category", "This is a test category")
        assert category.name == "Test Category"
        assert category.description == "This is a test category"

    def test_get_total_categories(self):
        Category.total_categories = 0  # Сброс перед тестом
        category1 = Category("Category 1", "Description 1")
        category2 = Category("Category 2", "Description 2")

        # Проверяем общее количество категорий
        assert Category.total_categories == 2

        # Используем созданные категории для проверки
        assert category1.name == "Category 1"
        assert category2.name == "Category 2"


if __name__ == "__main__":
    pytest.main()
