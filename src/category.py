from src.product import Product


class Category:
    """Класс для представления категории продуктов."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.__products = []  # Приватный атрибут

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        print(f"Продукт '{product.name}' добавлен в категорию '{self.name}'.")

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строк."""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_list)

    def list_products(self) -> None:
        """Выводит список продуктов в категории."""
        print(f"Продукты в категории '{self.name}':")
        print(self.products)  # Используем геттер для вывода списка


# class Category:
#     """Класс для представления категории продуктов."""
#     category_count = 0  # Количество категорий
#     product_count = 0  # Количество всех товаров
#
#     def __init__(self, name: str, description: str) -> None:
#         """
#         Инициализация объекта Category.
#
#         name: Название категории.
#         description: Описание категории.
#         """
#         self.name = name
#         self.description = description
#         self._products: List[Product] = []  # Приватный список продуктов
#         # Увеличиваем статические атрибуты класса
#         Category.category_count += 1
#
#     def add_product(self, product: Product) -> None:
#         """
#         Метод для добавления продукта в категорию.
#         product: Объект класса Product.
#         """
#         if not isinstance(product, Product):
#             raise TypeError("Можно добавлять только объекты класса Product или его подклассов.")
#         self._products.append(product)
#         Category.product_count += 1
#
#     @property
#     def products(self) -> str:
#         """
#         Геттер для получения списка продуктов.
#         Возвращает строку с описанием продуктов.
#         """
#         return "\n".join(
#             [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self._products]
#         )
