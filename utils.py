import json


def load_data_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Загружаем данные
data = load_data_from_json("data/products.json")

# Проверяем, что данные - это список
if isinstance(data, list):
    for category_data in data:
        # Теперь category_data - это словарь с данными категории
        category_name = category_data["name"]
        category_description = category_data["description"]
        products = category_data["products"]

        print(f"Категория: {category_name}")
        print(f"Описание: {category_description}")

        for product in products:
            product_name = product["name"]
            product_description = product["description"]
            product_price = product["price"]
            product_quantity = product["quantity"]

            print(f"  Продукт: {product_name}")
            print(f"  Описание: {product_description}")
            print(f"  Цена: {product_price}")
            print(f"  Количество: {product_quantity}")
else:
    print("Неправильная структура данных:", data)
