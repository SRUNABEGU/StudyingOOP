from abc import ABC, abstractmethod


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}({', '.join([repr(a) for a in args])})")  # pragma: no cover
        super().__init__() # pragma: no cover


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(MixinLog, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__(name, description, price, quantity)

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
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Добавлять в категорию можно только объекты Product или его наследников")
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
#     print("--- Проверка логирования ---")
#     p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
#     s1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "high", "15", 512, "Gray")
#     g1 = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Russia", "14 days", "Green")
#
#     print("\n--- Проверка абстрактного класса ---")
#     try:
#         bad_obj = BaseProduct()
#     except TypeError as e:
#         print(f"Ожидаемая ошибка: {e}")
#
#     print("\n--- Проверка Category и вывода ---")
#     category = Category("Электроника", "Техника")
#     category.add_product(p1)
#     category.add_product(s1)
#
#     print(category)
#     print(category.products)