import json

from src.classes import Category, Product


def read_json_file(file_path: str) -> list[dict]:
    """Функция для считывания информации из JSON-файла."""

    with open(file_path, "r", encoding="utf-8") as f:
        result = json.load(f)

    return result


def get_categories_and_products(data: list[dict]) -> list[Category]:
    """Возвращает список объектов класса Category."""

    list_of_categories = []

    for category in data:

        list_of_products = []

        for product in category["products"]:
            product = Product(product["name"], product["description"], product["price"], product["quantity"])
            list_of_products.append(product)

        category = Category(category["name"], category["description"], list_of_products)
        list_of_categories.append(category)

    return list_of_categories
