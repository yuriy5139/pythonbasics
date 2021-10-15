class Worker():
    def __init__(self, name="Джохн", surname="Сильвер", position="Пират", wage=100, bonus=50):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name="Джон", surname="Флинт", position="Пират", wage=100, bonus=50):
        super().__init__(name=name, surname=surname, position=position, wage=wage, bonus=bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == "__main__":
    captain = Position(name = "Джохн", surname="Сильвер", wage=200, bonus=100)
    print("Сотрудник {} в должности {} получает {} пиастров в месяц, это если вместе с бонусом, но грязными".format(
        captain.get_full_name(), captain.position, captain.get_total_income()
    ))
