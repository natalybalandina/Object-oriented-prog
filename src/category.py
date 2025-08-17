from .product import Product


class Category:
    # Атрибуты класса для хранения общего количества категорий и товаров
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        """
        Инициализация категории.
        name: Название категории (строка).
        description: Описание категории (строка).
        """
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = []  # Список товаров категории (список объектов класса Product)

        # Увеличиваем общее количество категорий
        Category.total_categories += 1

    def add_product(self, product: Product):
        """
        Добавление продукта в категорию.
        product: Объект класса Product для добавления в категорию.
        """
        self.products.append(product)  # Добавление продукта в список
        # Увеличиваем общее количество товаров
        Category.total_products += 1

    @classmethod
    def get_total_categories(cls):
        return cls.total_categories

    @classmethod
    def get_total_products(cls):
        return cls.total_products
