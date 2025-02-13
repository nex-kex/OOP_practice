from src.classes import Category


def test_product_init(product_phone):
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5


def test_category_init(category_phones):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Средство коммуникации"
    assert category_phones.products == ["Samsung", "Iphone", "Xiaomi"]
    assert Category.categories_count == 1
    assert Category.products_count == 3
