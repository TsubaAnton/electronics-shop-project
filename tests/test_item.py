"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0
    assert item1.price == 8000.0
    assert item2.price == 20000
    assert Item.all


def test_name_property():
    item = Item("Телефон", 10000, 5)
    assert item.name == "Телефон"

    item.name = "Длинное_название"
    assert item.name == "Длинное_на"


def test_instantiate_from_csv():
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_string_to_number():
    result = Item.string_to_number("5.7")
    assert result == 5



