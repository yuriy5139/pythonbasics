import random
from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self, items=None):
        self.__items = {}
        if items:
            try:
                iter(items)
                for item in items:
                    self.__items[item.idf] = item
            except TypeError as e:
                self.__items[items.idf] = items

    def add_units(self, items):
        try:
            iter(items)
            for item in items:
                if not item.idf in self.__items:
                    self.__items[item.idf] = item
                else:
                    print(f"Объект с идентификатором {item.idf} уже есть на складе. Используйте уникальный ID")
        except Exception as e:
            if not items.idf in self.__items:
                self.__items[items.idf] = items
            else:
                print(f"Объект с идентификатором {items.idf} уже есть на складе. Используйте уникальный ID")

    @property
    def items(self):
        return self.__items.items()

    @staticmethod
    def check_amount(amount):
        if amount <= 0:
            print("Количество юнитов должно быть положительным")
            return False
        return True

    def __str__(self):
        ln = ""
        for k, v in self.__items.items():
            ln += f"Предмет №{k}: {v}\n"
        return ln


class BaseUnit(ABC):
    def __init__(self, idf, name):
        self.__idf = idf
        self.__name = name
        self.__owner = None

    @property
    def idf(self):
        return (self.__idf)

    @property
    def name(self):
        return (self.__name)

    @property
    def owner(self):
        return (self.__owner)

    def set_owner(self, owner):
        self.__owner = owner

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def estimate_price(self):
        pass


class Printer(BaseUnit):
    def __init__(self, idf, name, toner_level):
        super().__init__(idf, name)
        self.__toner_level = toner_level

    @property
    def toner_level(self):
        return self.__toner_level

    def estimate_price(self):
        return 100 + self.toner_level

    def __str__(self):
        return f"На связи принтер {self.name} с идентификатором {self.idf}. Уровень тонера {self.toner_level}. Передан в отдел {self.owner}"


class Scanner(BaseUnit):
    def __init__(self, idf, name, dpi):
        super().__init__(idf, name)
        self.__dpi = dpi

    @property
    def dpi(self):
        return self.__dpi

    def estimate_price(self):
        return 200 + self.dpi

    def __str__(self):
        return f"На связи сканер {self.name} с идентификатором {self.idf}. Разрешение {self.dpi} точек на дюйм. Передан в отдел {self.owner}"


class Copier(BaseUnit):
    def __init__(self, idf, name, is_manual):
        super().__init__(idf, name)
        self.__is_manual = is_manual

    @property
    def is_manual(self):
        return self.__is_manual

    def estimate_price(self):
        return 300 + 100 * (not self.is_manual)

    def __str__(self):
        return f"На связи копир {self.name} с идентификатором {self.idf}. Автоматический? - {self.is_manual}. Передан в отдел {self.owner}"


if __name__ == "__main__":
    try:
        printers_num = int(input("введите количество принтеров "))
        scanners_num = int(input("введите количество сканеров "))
        copiers_num = int(input("введите количество копиров "))

        printers = [Printer(i, "printer_" + str(i), 100 - i * 5) for i in range(0, printers_num)]
        scanners = [Scanner(i, "scanner_" + str(i), 50 + i) for i in range(100, 100 + scanners_num)]
        copiers = [Copier(i, "copier_" + str(i), bool(i % 2)) for i in range(200, 200 + copiers_num)]

        if not Warehouse.check_amount(printers_num) or not Warehouse.check_amount(
                scanners_num) or not Warehouse.check_amount(copiers_num):
            print("Не пройдена проверка на корректность вводимых данных. Выходим.")
        else:
            ws = Warehouse(printers[0])
            print("\nИнициализирован склад:")
            print(ws)
            ws.add_units(scanners)
            ws.add_units(copiers)
            print("Склад после добавления сканеров и копиров:")
            print(ws)

            for idf, item in ws.items:
                owner = random.choice(["Бухгалтерия", "IT", "Менеджмент", "HR"])
                item.set_owner(owner)

            print("После распределения по отделам:")
            print(ws)

    except ValueError:
        print("Можно вводить только целые положительные числа! Выходим.")
    except Exception as e:
        print("И снова что-то не так!", e)
