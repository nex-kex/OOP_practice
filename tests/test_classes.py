from src.classes import Category


def test_product_init(product_phone):
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5


def test_category_init(category_phones, category_laptops):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Средство коммуникации"
    assert len(category_phones.products) == 3

    assert category_phones.category_count == 2
    assert category_laptops.category_count == 2
    assert Category.category_count == 2

    assert category_phones.product_count == 7
    assert category_laptops.product_count == 7
    assert Category.product_count == 7
