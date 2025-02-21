from unittest.mock import patch

from src.classes import Category, Product


def test_product_init(product_phone):
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5


def test_price_setter_zero(product_phone, capsys):
    product_phone.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_price_setter_new_lower_price_changed(product_phone, capsys):
    with patch("builtins.input", return_value="y"):
        product_phone.price = 100
        captured = capsys.readouterr()
        assert (
            captured.out
            == "Новая цена товара (100) ниже предыдущей (180000.0). Вы уверены, что вы хотите снизить цену? (y/n)\n"
        )
        assert product_phone.price == 100


def test_price_setter_new_lower_price_not_changed(product_phone, capsys):
    with patch("builtins.input", return_value="n"):
        product_phone.price = 100
        captured = capsys.readouterr()
        assert (
            captured.out
            == "Новая цена товара (100) ниже предыдущей (180000.0). Вы уверены, что вы хотите снизить цену? (y/n)\n"
        )
        assert product_phone.price == 180000.0


def test_price_setter_new_higher_price(product_phone):
    product_phone.price = 1000000.00
    assert product_phone.price == 1000000.00


def test_new_product():
    new_product = Product.new_product(
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    )
    assert new_product.name == '55" QLED 4K'
    assert new_product.description == "Фоновая подсветка"
    assert new_product.price == 123000.0
    assert new_product.quantity == 7

    assert len(new_product._Product__all_products) == 6


def test_new_new_product(product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 280000.0
    assert new_product.quantity == 8

    assert len(new_product._Product__all_products) == 6


def test_category_init(category_phones, category_laptops):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Средство коммуникации"
    assert (
        category_phones.products
        == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
"""
    )

    assert category_phones.category_count == 2
    assert category_laptops.category_count == 2
    assert Category.category_count == 2

    assert category_phones.product_count == 7
    assert category_laptops.product_count == 7
    assert Category.product_count == 7


def test_add_product(category_phones, product_phone):
    assert Category.product_count == 10
    category_phones.add_product(product_phone)
    assert Category.product_count == 11
