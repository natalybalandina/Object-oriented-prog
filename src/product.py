class Product:
    """Класс для представления продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация объекта Product.

        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продукта в наличии.
        ValueError: Если цена или количество отрицательные.
        """
        if price <= 0:
            raise ValueError("Цена товара не может быть нулевой или отрицательной")
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.__quantity = quantity  # Приватный атрибут количества

    @property
    def price(self) -> float:
        """Геттер для атрибута 'цена'."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута 'цена'."""
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")

        if new_price < self.__price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirmation.lower() != 'y':
                print("Изменение цены отменено.")
                return

        self.__price = new_price
        print(f"Цена успешно изменена на {self.__price}")

    @property
    def quantity(self) -> int:
        """Геттер для атрибута 'количество'."""
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        """Сеттер для атрибута 'количество'."""
        if new_quantity < 0:
            raise ValueError("Количество не должно быть отрицательным")
        self.__quantity = new_quantity

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list) -> 'Product':
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        for existing_product in existing_products:
            if existing_product.name == name:
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                print(f"Товар '{name}' уже существует. Обновлено количество до {existing_product.quantity} и цена до {existing_product.price}.")
                return existing_product

        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        existing_products.append(new_product)
        print(f"Создан новый продукт: {new_product.name}")

        return new_product
