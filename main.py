from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    for product in [product1, product2, product3]:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
    )
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1.name)
    print(category1.description)
    print(len(category1.products))

    product4 = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
    )
    category2.add_product(product4)

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
