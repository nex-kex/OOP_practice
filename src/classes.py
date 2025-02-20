from typing import Any


class Product:
    """Класс для представления продуктов."""

    __all_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.__all_products.append(self)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            print(
                f"Новая цена товара ({new_price}) ниже предыдущей ({self.__price}). \
Вы уверены, что вы хотите снизить цену? (y/n)"
            )
            answer = input()
            if answer == "y":
                self.__price = new_price
        elif new_price >= self.__price:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_dict: dict) -> Any:

        name = product_dict["name"]
        for product in Product.__all_products:

            if product.name == name:
                product.quantity += product_dict["quantity"]

                if product.price != product_dict["price"]:
                    product.__price = max(product.price, product_dict["price"])

                return product

        return Product(**product_dict)


class Category:
    """Класс для представления категорий продуктов."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = []):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return self.__products
