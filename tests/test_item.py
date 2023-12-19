"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def setup_items():
    Item.all = []
    Item.pay_rate = 1.0


def test_calculate_total_price(setup_items):
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(setup_items):
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0
    assert item1.price == 8000.0
    assert item2.price == 20000
    assert Item.all


def test_name_property(setup_items):
    item = Item("Телефон", 10000, 5)
    assert item.name == "Телефон"

    item.name = "Длинное_название"
    assert item.name == "Длинное_на"


def test_instantiate_from_csv(setup_items):
    Item.instantiate_from_csv(r'C:\Users\onton\PycharmProjects\electronics-shop-project\src\items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_string_to_number():
    result = Item.string_to_number("5.7")
    assert result == 5



