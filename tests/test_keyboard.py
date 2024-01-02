import pytest
from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark KD87A', 9600, 5)
    assert kb.name == 'Dark KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == 'EN'


def test_language_change():
    kb = Keyboard('Dark KD87A', 9600, 5)

    kb.change_lang()
    assert kb.language == 'RU'

    kb.change_lang()
    assert kb.language == 'EN'


def test_string_representation():
    kb = Keyboard('Dark KD87A', 9600, 5)
    assert str(kb) == 'Dark KD87A'


def test_set_language_error():
    kb = Keyboard('Dark KD87A', 9600, 5)

    with pytest.raises(AttributeError, match="property 'language' of 'Keyboard' object has no setter"):
        kb.language = 'CH'
