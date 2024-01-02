from src.item import Item


class MixinLog:

    def __init__(self):
        self._language = 'EN'
        super().__init__()

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self) -> str:
        return self._language

    def __str__(self):
        return f"{self.name}"

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
        else:
            self._language = "EN"
        return self

    @language.setter
    def language(self, value):
        if value not in {'EN', 'RU'}:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self._language = value





