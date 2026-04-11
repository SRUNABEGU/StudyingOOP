import pytest
from main import Category, Product, Smartphone, LawnGrass, BaseProduct


@pytest.fixture()
def product_pencil() -> Product:
    return Product("Карандаш", "Простой карандаш", 20.0, 10)


@pytest.fixture()
def category_writing_instruments(product_pencil) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Письменные принадлежности",
        "Все для письма",
        [product_pencil],
    )


def test_product_init(product_pencil):
    assert product_pencil.name == "Карандаш"
    assert product_pencil.price == 20.0


def test_product_price_setter(product_pencil):
    product_pencil.price = 30.0
    assert product_pencil.price == 30.0
    product_pencil.price = -5.0
    assert product_pencil.price == 30.0


def test_new_product_classmethod():
    data = {"name": "Ручка", "description": "Гелевая", "price": 100.0, "quantity": 5}
    new_prod = Product.new_product(data)
    assert new_prod.name == "Ручка"
    assert new_prod.price == 100.0


def test_category_products_format(category_writing_instruments):
    expected_output = "Карандаш, 20.0 руб. Остаток: 10 шт."
    assert category_writing_instruments.products == expected_output


def test_category_counts(category_writing_instruments):
    assert Category.category_count == 1
    assert Category.product_count == 1
    new_p = Product("Линейка", "30см", 50.0, 2)
    category_writing_instruments.add_product(new_p)
    assert Category.product_count == 2


def test_product_str(product_pencil):
    assert str(product_pencil) == "Карандаш, 20.0 руб. Остаток: 10 шт."


def test_category_str(category_writing_instruments):
    assert str(category_writing_instruments) == "Письменные принадлежности, количество продуктов: 10 шт."


def test_product_add():
    p1 = Product("Товар 1", "Оп", 100.0, 10)
    p2 = Product("Товар 2", "Оп", 100.0, 5)
    assert p1 + p2 == 1500.0


def test_smartphone_init():
    smart = Smartphone("iPhone 15", "Gray", 100000.0, 5, "high", "15", 128, "Gray")
    assert smart.name == "iPhone 15"


def test_lawngrass_init():
    grass = LawnGrass("Трава", "Зеленая", 100.0, 1, "USA", "10 days", "Green")
    assert grass.country == "USA"


def test_addition_type_error():
    smart = Smartphone("iPhone 15", "Gray", 100000.0, 5, "high", "15", 128, "Gray")
    grass = LawnGrass("Медонос", "Зеленая", 500.0, 10, "Russia", "14 days", "Green")
    with pytest.raises(TypeError):
        _ = smart + grass


def test_category_add_invalid_object():
    cat = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("Не продукт")

def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct()
