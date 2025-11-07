import pytest
from src.main import Category, Product


@pytest.fixture()
def product_pencil() -> Product:
    return Product("Карандаш", "Простой карандаш, прямой, наточен", 20.0, 1)


def test_init(product_pencil) -> None:
    """lol"""
    assert product_pencil.name == "Карандаш"
    assert product_pencil.description == "Простой карандаш, прямой, наточен"
    assert product_pencil.price == 20.0
    assert product_pencil.quantity == 1


@pytest.fixture()
def category_writing_instruments(product_pencil) -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Письменные принадлежности",
        "Письменные принадлежности...Карандаши, там, ручки",
        [product_pencil],
    )


def test_category_writing_instruments(category_writing_instruments, product_pencil) -> None:
    assert category_writing_instruments.name == "Письменные принадлежности"
    assert (
        category_writing_instruments.description
        == "Письменные принадлежности...Карандаши, там, ручки"
    )
    assert category_writing_instruments.products == [product_pencil]
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_multiple_categories_and_products() -> None:
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Ручка", "Синяя гелевая ручка", 50.0, 10)
    product2 = Product("Маркер", "Желтый маркер для выделения текста", 70.0, 5)
    product3 = Product("Тетрадь", "96 листов, клетка", 100.0, 3)

    assert Category.category_count == 0
    assert Category.product_count == 0

    category1 = Category("Ручки и маркеры", "Все для письма", [product1, product2])
    category2 = Category("Бумажная продукция", "Тетради, блокноты", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3
