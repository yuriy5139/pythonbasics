class Matrix:
    def __init__(self, rank2):
        """
        Матрица второго порядка - список списков.
        Каждый список - это строка матрицы

        :param rank2: список списков.
        """
        self.rank2 = rank2

    def __str__(self):
        result = "["
        for ln in self.rank2:
            prnln = "["
            for el in ln:
                prnln += str(el) + ", "
            prnln += "]\n"
            result += prnln
        result = result.replace(", ]", "]")
        return result[:-1] + "]"

    @property
    def shape(self):
        return len(self.rank2), len(self.rank2[0])

    def __add__(self, other):
        """
        Поэлементное сложение матриц. Суммируемая матрица должна иметь такую же размерность, как и
        исходная.
        :param other: суммируемая матрица
        :return: объект Matrix
        """
        if not self.shape == other.shape:
            print("Возможно сложение только одноранговых матриц")
        else:
            result = []
            for ln in zip(self.rank2, other.rank2):
                newline = []
                for i in range(len(ln[0])):
                    newline.append(ln[0][i] + ln[1][i])
                result.append(newline)
        return Matrix(result)


if __name__ == "__main__":
    stub1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
    m1 = Matrix(stub1)
    stub2 = [[1, 2, 3], [0, 0, 0], [-1, -2, -3], [9, 10, 11]]
    m2 = Matrix(stub2)
    stub3 = [[1, 1, 1], [2, 2, 2], [3, 2, 1], [-1, -1, -1]]
    m3 = Matrix(stub3)

    m3 = m1 + m2 + m3
    print(m3)
