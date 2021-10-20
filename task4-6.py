class Warehouse:
    def __init__(self, items):
        self.__items = {}
        try:
            iter(items)
            for item in items:
                self.__items[item.idf] = item
        except Exception as e:
            self.__items[items.idf] = items

    def add_units(self, items):
        try:
            iter(items)
            for item in items:
                if not item.idf in self.__items:
                    self.__items[item.idf] = item
        except Exception as e:
            if not items.idf in self.__items:
                self.__items[items.idf] = items

    @property
    def items(self):
        for k, v in self.__items.items():
            print(f"Предмет №{k}: {v}")

class BaseUnit:
    def __init__(self, idf):
        self.__idf = idf

    def __str__(self):
        return f"Объект класса BaseUnit с идентификатором {self.idf}"

    @property
    def idf(self):
        return (self.__idf)


if __name__ == "__main__":
    unit1 = BaseUnit(1)
    unit2 = BaseUnit(2)
    unit3 = BaseUnit(3)
    wh = Warehouse([unit2, unit3])
    wh.add_units(unit1)
    wh.items
