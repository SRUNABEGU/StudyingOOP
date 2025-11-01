import pytest
from main import Category, Product


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
