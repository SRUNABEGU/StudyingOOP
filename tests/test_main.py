import pytest
from src.main import Category, Product, Smartphone, LawnGrass


@pytest.fixture()
def product_pencil() -> Product:
    return Product("Карандаш", "Простой карандаш", 20.0, 10)


@pytest.fixture()
def category_writing_instruments(product_pencil) -> Category:
    # Сбрасываем счетчики перед тестом, чтобы они не копились
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Письменные принадлежности",
        "Все для письма",
        [product_pencil],
    )


def test_product_init(product_pencil):
    """Проверяем инициализацию товара и работу геттера цены"""
    assert product_pencil.name == "Карандаш"
    assert product_pencil.price == 20.0


def test_product_price_setter(product_pencil):
    """Тестируем логику изменения цены"""
    product_pencil.price = 30.0
    assert product_pencil.price == 30.0

    # Проверка на отрицательную цену (не должна измениться)
    product_pencil.price = -5.0
    assert product_pencil.price == 30.0


def test_new_product_classmethod():
    """Тестируем создание товара из словаря"""
    data = {"name": "Ручка", "description": "Гелевая", "price": 100.0, "quantity": 5}
    new_prod = Product.new_product(data)
    assert new_prod.name == "Ручка"
    assert new_prod.price == 100.0


def test_category_products_format(category_writing_instruments):
    """Тестируем геттер, который возвращает строки"""
    expected_output = "Карандаш, 20.0 руб. Остаток: 10 шт."
    assert category_writing_instruments.products == expected_output


def test_category_counts(category_writing_instruments):
    """Проверяем счетчики категорий и товаров"""
    assert Category.category_count == 1
    assert Category.product_count == 1

    # Добавим еще товар
    new_p = Product("Линейка", "30см", 50.0, 2)
    category_writing_instruments.add_product(new_p)
    assert Category.product_count == 2


def test_product_str(product_pencil):
    """Проверка строкового отображения товара"""
    assert str(product_pencil) == "Карандаш, 20.0 руб. Остаток: 10 шт."


def test_category_str(category_writing_instruments):
    """Проверка строкового отображения категории (сумма всех шт.)"""
    assert str(category_writing_instruments) == "Письменные принадлежности, количество продуктов: 10 шт."


def test_product_add():
    """Проверка сложения двух товаров одного класса"""
    p1 = Product("Товар A", "Описание", 100.0, 10)  # 100 * 10 = 1000
    p2 = Product("Товар B", "Описание", 100.0, 2)   # 100 * 2 = 200
    assert p1 + p2 == 1200.0


def test_smartphone_init():
    """Тест инициализации смартфона"""
    smart = Smartphone("iPhone 15", "Gray", 100000.0, 5, "high", "15", 128, "Gray")
    assert smart.name == "iPhone 15"
    assert smart.memory == 128


def test_lawngrass_init():
    """Тест инициализации травы"""
    grass = LawnGrass("Трава", "Зеленая", 100.0, 1, "USA", "10 days", "Green")
    assert grass.country == "USA"


def test_addition_type_error():
    """Проверка ошибки при сложении разных классов"""
    smart = Smartphone("iPhone 15", "Gray", 100000.0, 5, "high", "15", 128, "Gray")
    grass = LawnGrass("Медонос", "Зеленая", 500.0, 10, "Russia", "14 days", "Green")
    with pytest.raises(TypeError):
        _ = smart + grass


def test_category_add_invalid_object():
    """Проверка ошибки при добавлении в категорию не-продукта"""
    cat = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("Не продукт")


def test_addition_same_type():
    """Проверка сложения смартфонов"""
    smart1 = Smartphone("iPhone 15", "Gray", 100000.0, 2, "high", "15", 128, "Gray")
    smart2 = Smartphone("Samsung", "Black", 80000.0, 3, "high", "S23", 256, "Black")
    assert smart1 + smart2 == 440000.0