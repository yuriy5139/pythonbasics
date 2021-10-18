class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __str__(self):
        return "Class <Cell>, {} partitions".format(self.parts)

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        if self.parts - other.parts >= 0:
            return Cell(self.parts - other.parts)
        else:
            print("Вычитаемая клетка больше уменьшаемой! Не надо!")

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, num):
        for part in range(1, self.parts + 1):
            print("*", end='')
            if part % num == 0:
                print("\n")


if __name__ == "__main__":
    cell1 = Cell(11)
    cell2 = Cell(20)
    print("cell1: ", cell1)
    print("cell2: ", cell2)
    cell3 = cell1 + cell2
    print("cell3: ", cell3)
    cell4 = cell1 - cell2
    cell4 = cell3 - cell2
    print("cell4: ", cell4)
    cell5 = cell1 * cell1
    print("cell5: ", cell5)
    cell6 = cell5 / cell2
    print("cell6: ", cell6)
    cell5.make_order(17)
