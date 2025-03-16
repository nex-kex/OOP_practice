import pytest

from src.classes import Category, Product


@pytest.fixture
def product_phone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_phones():
    return Category(
        name="Смартфоны",
        description="Средство коммуникации",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category_laptops():
    return Category(
        name="Ноутбуки",
        description="Переносные компьютеры",
        products=[
            Product("Lenovo IdeaPad 3", '256GB, Серый цвет, 15.6"', 450000.0, 4),
            Product("ASUS VivoBook 15", '512GB, Чёрный цвет, 15.6"', 550000.0, 3),
            Product("Acer Nitro 5", '512GB, Серый цвет, 15.6"', 90000.0, 9),
            Product("HP Pavilion 14", '512GB, Синий цвет, 14"', 60000.0, 7),
        ],
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 280000.0,
        "quantity": 3,
    }
