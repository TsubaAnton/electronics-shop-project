import csv
import os


class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке при создании объектов из CSV файла.
    """
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file_path=None):
        """
        Создание объектов из данных файла.

        :param file_path: Путь к CSV файлу.
        """
        cls.all = []
        required_columns = ['name', 'price', 'quantity']

        try:
            if file_path is None:
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.csv')
            with open(file_path, 'r+', encoding='windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)

                # Проверяем, что все требуемые колонки присутствуют в заголовке CSV файла
                if not all(column in reader.fieldnames for column in required_columns):
                    raise InstantiateCSVError("Файл items.csv поврежден")

                for row in reader:
                    try:
                        name = row['name']
                        price = float(row['price'])

                        # Проверяем наличие значений во всех необходимых колонках
                        if any(row[column] is None for column in required_columns):
                            raise InstantiateCSVError("Файл items.csv поврежден")

                        quantity = int(row['quantity'])
                        cls(name, price, quantity)
                    except (KeyError, ValueError):
                        raise InstantiateCSVError("Файл items.csv поврежден")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise FileNotFoundError(f"Отсутствует файл {file_path}")
        except csv.Error:
            raise InstantiateCSVError("Файл items.csv поврежден")

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Возвращает число из числа-строки.
        """
        return int(float(value))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError("Можно складывать только экземпляры классов Item")
        return self.quantity + other.quantity