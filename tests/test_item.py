"""Здесь надо написать тесты с использованием pytest для модуля item."""
import re
import pytest
import os
from src.item import Item, InstantiateCSVError


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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, '..', 'src', 'items.csv')

    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_string_to_number():
    result = Item.string_to_number("5.7")
    assert result == 5


def test_item_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add_items(setup_items):
    item1 = Item("Лампа", 500, 10)
    item2 = Item("Ноутбук", 20000, 5)

    result = item1 + item2
    assert result == 15


def test_add_items_with_discount(setup_items):
    item1 = Item("Лампа", 500, 10)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8

    result = item1 + item2
    assert result == 15


def test_add_non_item_instance(setup_items):
    item1 = Item("Лампа", 500, 10)
    phone = "Смартфон"

    with pytest.raises(TypeError, match="Можно складывать только экземпляры классов Item"):
        result = item1 + phone


def test_exp_from_csv_file(tmp_path):
    filedir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(filedir, '..', 'src', 'items2.csv')

    with pytest.raises(FileNotFoundError, match=f"Отсутствует файл {re.escape(csv_path)}"):
        Item.instantiate_from_csv(file_path=csv_path)


def test_check_columns_in_csv(tmp_path):
    filedir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(filedir, '..', 'src', 'items1.csv')

    with pytest.raises(InstantiateCSVError, match="Файл items.csv поврежден"):
        Item.instantiate_from_csv(file_path=csv_path)
