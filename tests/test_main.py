import pytest
from src.main import Category, Product


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
    """Тестируем логику изменения цены (Задание 4)"""
    product_pencil.price = 30.0
    assert product_pencil.price == 30.0

    # Проверка на отрицательную цену (не должна измениться)
    product_pencil.price = -5.0
    assert product_pencil.price == 30.0


def test_new_product_classmethod():
    """Тестируем создание товара из словаря (Задание 3)"""
    data = {"name": "Ручка", "description": "Гелевая", "price": 100.0, "quantity": 5}
    new_prod = Product.new_product(data)
    assert new_prod.name == "Ручка"
    assert new_prod.price == 100.0


def test_category_products_format(category_writing_instruments):
    """Тестируем геттер, который возвращает строки (Задание 2)"""
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
    # В фикстуре 1 карандаш (10 шт.)
    assert str(category_writing_instruments) == "Письменные принадлежности, количество продуктов: 10 шт."

def test_product_add():
    """Проверка сложения двух товаров"""
    p1 = Product("Товар A", "Описание", 100.0, 10)  # 100 * 10 = 1000
    p2 = Product("Товар B", "Описание", 200.0, 2)   # 200 * 2 = 400
    assert p1 + p2 == 1400.0

def test_category_products_getter(category_writing_instruments):
    """Проверка, что геттер всё еще выдает правильную строку"""
    assert category_writing_instruments.products == "Карандаш, 20.0 руб. Остаток: 10 шт."