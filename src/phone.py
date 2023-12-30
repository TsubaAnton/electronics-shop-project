from src.item import Item


class Phone(Item):
    """Класс для представления телефона в магазине"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = None
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self._number_of_sim = value

    def __add__(self, other):
        """Метод сложения экземпляров классов Phone и Item"""
        if not isinstance(other, (Phone, Item)):
            raise TypeError("Можно складывать только экземпляры классов Phone и Item")
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
