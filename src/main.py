class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_strings = [str(product) for product in self.__products]
        return "\n".join(product_strings)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


# if __name__ == "__main__":
#     p1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
#     p2 = Product("Iphone 15", "512GB", 210000.0, 8)
#
#     cat = Category("Смартфоны", "Описание", [p1, p2])
#
#     print(p1)  # Выведет: Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
#     print(cat)  # Выведет: Смартфоны, количество продуктов: 13 шт.
#     print(f"Общая стоимость на складе: {p1 + p2}")  # Выведет: 2580000.0