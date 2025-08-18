import pytest

from src.product import Product


class TestProduct:
    @pytest.fixture
    def product(self):
        """Создаем экземпляр продукта для тестирования."""
        return Product(
            name="Test Product",
            description="This is a test product.",
            price=100.0,
            quantity=10,
        )

    def test_initialization(self, product):
        """Тестируем правильную инициализацию объекта Product."""
        assert product.name == "Test Product"
        assert product.description == "This is a test product."
        assert product.price == 100.0
        assert product.quantity == 10

    def test_price_setter(self, product):
        """Тестируем установку цены."""
        product.price = 120.0
        assert product.price == 120.0

    def test_price_setter_negative(self, product):
        """Тестируем установку отрицательной цены."""
        with pytest.raises(ValueError):
            product.price = -50.0

    def test_quantity_setter(self, product):
        """Тестируем установку количества."""
        product.quantity = 15
        assert product.quantity == 15

    def test_quantity_setter_negative(self, product):
        """Тестируем установку отрицательного количества."""
        with pytest.raises(ValueError):
            product.quantity = -5

    def test_new_product_creation(self):
        """Тестируем создание нового продукта через метод new_product."""
        existing_products = []
        product_data = {
            "name": "New Product",
            "description": "This is a new product.",
            "price": 50.0,
            "quantity": 5,
        }

        new_product = Product.new_product(product_data, existing_products)

        assert new_product.name == "New Product"
        assert new_product.description == "This is a new product."
        assert new_product.price == 50.0
        assert new_product.quantity == 5
