class Product:
    """Класс для представления продуктов."""

    __all_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.__all_products.append(self)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input(f"Новая цена товара ({new_price}) ниже предыдущей ({self.__price}). Вы уверены, что вы хотите снизить цену? (y/n) ")
            if answer == "y":
                self.__price = new_price


    @classmethod
    def new_product(cls, product_dict):

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


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return self.__products
