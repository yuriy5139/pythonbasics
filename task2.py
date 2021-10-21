class ZeroDivisionError(BaseException):
    """
    Переписали класс-исключение, который вызывается интерпретатором при делении на ноль
    Поменяли только реализацию __string__

    """

    def __str__(self):
        return ("ZeroDivisionError после ребрендинга. С вас $20 000")


if __name__ == "__main__":
    denominator = int(input("введите делитель "))
    try:
        1 / denominator
    except BaseException as e:
        print(e)

    print("не получилось :(\n")

    try:
        if denominator == 0:
            raise ZeroDivisionError()
    except BaseException as e:
        print(e)

    print("получилось :)\n")
