import json
import os

from src.classes import Category, Product


def read_json_file(file_path: str) -> list:
    """Функция для считывания информации из JSON-файла."""
    full_path = os.path.abspath(file_path)

    with open(full_path, "r", encoding="utf-8") as f:
        return list(json.load(f))


def get_categories_and_products(data: list[dict]) -> list[Category]:
    """Возвращает список объектов класса Category."""

    list_of_categories = []

    for category in data:

        list_of_products = []

        for product in category["products"]:
            list_of_products.append(Product(**product))

        list_of_categories.append(Category(**category))

    return list_of_categories


if __name__ == "__main__":
    raw_data = read_json_file("../data/products.json")
    all_categories = get_categories_and_products(raw_data)
    for category in all_categories:
        print(category.products, end=" ")
        print()
