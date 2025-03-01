from typing import Any


class Product:
    """Класс для представления продуктов."""

    all_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if issubclass(type(other), Product):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError("Можно складывать только товары одного типа.")

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
        for product in Product.all_products:

            if product.name == name:
                product.quantity += product_dict["quantity"]

                if product.price != product_dict["price"]:
                    product.__price = max(product.price, product_dict["price"])

                return product

        return Product(**product_dict)


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> Any:
        if issubclass(type(other), Smartphone):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Можно складывать только товары одного типа.")


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Any) -> Any:
        if issubclass(type(other), LawnGrass):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Можно складывать только товары одного типа.")


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

    def __str__(self) -> str:
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, product: object) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно создавать категории только из продуктов.")

    @property
    def products(self) -> list:
        answer = []
        for product in self.__products:
            answer.append(str(product))
        return answer


class CategoryIteration:

    def __init__(self, my_category: Category):
        self.products = my_category.products
        self.end = len(self.products)

    def __iter__(self) -> Any:
        self.current_index = -1
        return self

    def __next__(self) -> Any:
        if self.current_index + 1 < self.end:
            self.current_index += 1
            return self.products[self.current_index]
        else:
            raise StopIteration

    def __getitem__(self, index: int) -> Any:
        return self.products[index]
