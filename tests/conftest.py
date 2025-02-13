import pytest

from src.classes import Category, Product


@pytest.fixture
def product_phone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category_phones():
    return Category("Смартфоны", "Средство коммуникации", ["Samsung", "Iphone", "Xiaomi"])
