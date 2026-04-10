from src.shop import Category, BaseProduct, LawnGrass, Smartphone, Product

if __name__ == "__main__":
    print("--- Проверка логирования ---")
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    s1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "high", "15", 512, "Gray")
    g1 = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Russia", "14 days", "Green")

    print("\n--- Проверка абстрактного класса ---")
    try:
        bad_obj = BaseProduct()
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")

    print("\n--- Проверка Category и вывода ---")
    category = Category("Электроника", "Техника")
    category.add_product(p1)
    category.add_product(s1)

    print(category)
    print(category.products)