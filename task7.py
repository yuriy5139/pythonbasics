class Cnumber:
    def __init__(self, *args):
        if isinstance(args[0], tuple) and len(args[0]) == 2:
            if Cnumber.validate(args[0][0], args[0][1]):
                self._a = args[0][0]
                self._b = args[0][1]
                self._number = (args[0][0], args[0][1])
        elif len(args) == 2:
            if Cnumber.validate(args[0], args[1]):
                self._a = args[0]
                self._b = args[1]
                self._number = (args[0], args[1])
        else:
            print("В конструктор можно передать либо кортеж из двух float или целых, либо два float или целых числа как параметры")

    @staticmethod
    def validate(*args):
        if isinstance(args[0], tuple) and len(args[0]) == 2:
            if isinstance(args[0][0], (int, float)) and isinstance(args[0][1], (int, float)):
                return True
            return False
        elif len(args) == 2:
            if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
                return True
            return False
        else:
            print("В действительной и мнимой частях можно использовать только целые числа или числа типа float")
            return False

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, ab_tuple):
        if Cnumber.validate(*ab_tuple):
            self._a = ab_tuple[0]
            self._b = ab_tuple[1]
            self._number = ab_tuple

    def __str__(self):
        return f"{self.a} + {self.b}i" if self.b > 0 else f"{self.a} - {self.b}i"

    def __add__(self, other):
        return Cnumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Cnumber(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)


if __name__ == "__main__":
    print("Из кортежа:")
    n1tuple = (2, 3)
    n1 = Cnumber(n1tuple)
    print(n1)
    print("\nИз действительной и мнимой частей")
    a, b = 3 , 4
    n2 = Cnumber(a, b)
    print(n2)
    print("\nСложение")
    n3 = n1 + n2
    print(f"n1({n1}) + n2({n2}) = {n3}")
    print("\nУмножение")
    n4 = n1*n2
    print(f"n1({n1}) * n2({n2}) = {n4}")

    print("\nПрисвоение (разрешаем присваивать только через кортеж)")
    ab_tuple = (0.5, 0.5)
    n1.number = ab_tuple
    print(n1)

    print("\nПробуем некорректную операцию")
    n5 = Cnumber("2 + 3i")
