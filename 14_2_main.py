from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    # Добавляем продукты в категорию
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    # Выводим список продуктов в категории
    print("Продукты в категории:")
    print(category1.products)

    # Создаем новый продукт и добавляем его в категорию
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # Выводим обновленный список продуктов в категории
    print("\nОбновленный список продуктов в категории:")
    print(category1.products)

    # Выводим количество продуктов в категории
    print(f"\nКоличество продуктов в категории: {len(category1.products.splitlines())}")

    # Создаем новый продукт через класс-метод new_product
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5},
        [product1, product2, product3]  # Передаем существующие продукты для проверки
    )

    # Выводим детали нового продукта
    print(f"\nНовый продукт: {new_product.name}, {new_product.description}, {new_product.price} руб., {new_product.quantity} шт.")

    # Изменяем цену нового продукта
    new_product.price = 800
    print(f"Измененная цена: {new_product.price}")

    # Проверяем поведение при попытке установить отрицательную цену
    new_product.price = -100
    print(f"Цена после попытки установить отрицательную: {new_product.price}")

    # Проверяем поведение при попытке установить нулевую цену
    new_product.price = 0
    print(f"Цена после попытки установить нулевую: {new_product.price}")
