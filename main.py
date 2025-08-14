class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.
        name: Название продукта (строка).
        description: Описание продукта (строка).
        price: Цена продукта (число с плавающей точкой, может содержать копейки).
        quantity: Количество продукта (целое число, измеряемое в штуках).
        """
        self.name = name  # Название продукта
        self.description = description  # Описание продукта
        self.price = price  # Цена продукта
        self.quantity = quantity  # Количество продукта

    def __str__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"


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


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1.name)
    print(category1.description)
    print(len(category1.products))

    product4 = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    category2.add_product(product4)

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
