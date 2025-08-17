import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import create_objects_from_json, read_json

# Данные для теста
mock_json_data = """
[
    {
        "name": "Electronics",
        "description": "Devices and gadgets",
        "products": [
            {"name": "Smartphone", "description": "Latest model", "price": 699.99, "quantity": 50},
            {"name": "Laptop", "description": "High performance", "price": 999.99, "quantity": 30}
        ]
    },
    {
        "name": "Home Appliances",
        "description": "Essential home devices",
        "products": [
            {"name": "Vacuum Cleaner", "description": "Powerful suction", "price": 199.99, "quantity": 20}
        ]
    }
]
"""


def test_read_json():
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_json("dummy_path.json")
        expected_result = json.loads(mock_json_data)
        assert result == expected_result


def test_create_objects_from_json():
    data = json.loads(mock_json_data)
    categories = create_objects_from_json(data)

    # Проверка количества созданных категорий
    assert len(categories) == 2

    # Проверка первой категории
    assert categories[0].name == "Electronics"
    assert categories[0].description == "Devices and gadgets"
    assert len(categories[0].products) == 2

    # Проверка первого продукта в первой категории
    assert categories[0].products[0].name == "Smartphone"
    assert categories[0].products[0].price == 699.99

    # Проверка второй категории
    assert categories[1].name == "Home Appliances"
    assert categories[1].description == "Essential home devices"
    assert len(categories[1].products) == 1

    # Проверка продукта в второй категории
    assert categories[1].products[0].name == "Vacuum Cleaner"
    assert categories[1].products[0].price == 199.99


if __name__ == "__main__":
    pytest.main()
