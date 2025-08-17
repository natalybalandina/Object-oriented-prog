class Product:
    total_products = 0


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
        Product.total_products += 1  # Увеличиваем счетчик при создании нового продукта

    def __str__(self):
        return (
            f"Product(name={self.name}, description={self.description}, "
            f"price={self.price}, quantity={self.quantity})"
        )
