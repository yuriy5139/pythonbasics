class Stationery():
    def __init__(self, title="Stationery"):
        self.title = title

    def draw(self):
        pass


class Pen(Stationery):
    def __init__(self, title="Pen"):
        super().__init__(title=title)

    def draw(self):
        print("Отрисовываю ручкой")


class Pencil(Stationery):
    def __init__(self, title="Pencil"):
        super().__init__(title=title)

    def draw(self):
        print("Отрисовываю карандашом")


class Handle(Stationery):
    def __init__(self, title="Handle"):
        super().__init__(title=title)

    def draw(self):
        print("Отрисовываю маркером")


if __name__ == "__main__":
    ruchka, karandash, marker = Pen(), Pencil(), Handle()

    for item in ruchka, karandash, marker:
        item.draw()
