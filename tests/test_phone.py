import pytest
from src.item import Item
from src.phone import Phone


def test_phone_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add_phone_and_item():
    phone = Phone("iPhone 14", 100000, 5, 2)
    item = Item("Headphones", 2000, 3)

    assert phone + item == 8


def test_two_phones():
    phone = Phone("iPhone 14", 100000, 5, 2)

    assert phone + phone == 10


def test_set_negative_sim_raises_value_error():
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля"):
        phone = Phone("Samsung Galaxy", 50000, 5, 2)
        phone.number_of_sim = 0
