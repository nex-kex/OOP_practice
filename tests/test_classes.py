from unittest.mock import patch

import pytest

from src.classes import Category, CategoryIteration, LawnGrass, Order, Product, Smartphone

# Product tests


def test_product_init(product_phone):
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5

    with pytest.raises(ValueError):
        product1 = Product("name", "description", 100, 0)


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
    Product.all_products = []
    new_product = Product.new_product(
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    )
    assert new_product.name == '55" QLED 4K'
    assert new_product.description == "Фоновая подсветка"
    assert new_product.price == 123000.0
    assert new_product.quantity == 7

    assert len(new_product.all_products) == 1


def test_new_new_product(product_phone, product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 280000.0
    assert new_product.quantity == 8

    assert len(new_product.all_products) == 2


def test_product_add():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert product1 + product2 == 5 * 180000.0 + 8 * 210000.0

    with pytest.raises(TypeError):
        product1 + 100


# Smartphone tests


def test_smartphone_init(product_phone):
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    assert smartphone1 + smartphone2 == 5 * 180000.0 + 8 * 210000.0

    with pytest.raises(TypeError):
        smartphone1 + 100


# LawnGrass tests


def test_lawngrass_init(product_phone):
    lawngrass1 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    assert lawngrass1.name == "Газонная трава 2"
    assert lawngrass1.description == "Выносливая трава"
    assert lawngrass1.price == 450.0
    assert lawngrass1.quantity == 15
    assert lawngrass1.country == "США"
    assert lawngrass1.germination_period == "5 дней"
    assert lawngrass1.color == "Темно-зеленый"


def test_lawngrass_add():
    lawngrass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    lawngrass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    assert lawngrass1 + lawngrass2 == 20 * 500.0 + 15 * 450.0

    with pytest.raises(TypeError):
        lawngrass1 + 100


# Category tests


def test_category_init(category_phones, category_laptops, product_phone):
    assert category_phones.name == "Смартфоны"
    assert category_phones.description == "Средство коммуникации"
    assert category_phones.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]

    assert category_phones.category_count == 2
    assert category_laptops.category_count == 2
    assert Category.category_count == 2

    assert category_phones.product_count == 7
    assert category_laptops.product_count == 7
    assert Category.product_count == 7

    category_phones.add_product(product_phone)
    assert Category.product_count == 8

    with pytest.raises(TypeError):
        category_phones.add_product(100)


def test_category_str():
    Category.product_count = 0
    Category.category_count = 0

    phones = Category(
        name="Смартфоны",
        description="Средство коммуникации",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )

    assert str(phones) == """Смартфоны, количество продуктов: 27 шт."""


def test_middle_price(category_laptops):
    assert category_laptops.middle_price() == 287500.0

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0.0


def test_category_iteration_init():
    Category.product_count = 0
    Category.category_count = 0

    category_iterator = CategoryIteration(
        Category(
            name="Смартфоны",
            description="Средство коммуникации",
            products=[
                Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
                Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
            ],
        )
    )

    assert category_iterator.end == 3

    category_list = list(str(x) for x in category_iterator)
    assert category_list == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
    assert str(category_iterator[2]) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


# Order tests


def test_order_init(product_phone):
    order1 = Order(product_phone, 12)
    assert order1.product == product_phone
    assert order1.amount == 12
    assert order1.price == product_phone.price * 12

    assert str(order1) == 'Заказ на "Samsung Galaxy S23 Ultra": 12 шт. на общую стоимость 2160000.0 руб.'
