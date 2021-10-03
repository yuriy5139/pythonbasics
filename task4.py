# С помощью **

def my_func(x, y):
    if not isinstance(x, float) or x <= 0 or not isinstance(y, int) or y >= 0:
        print("x - неотрицательный float, y - отрицательный int")
        return
    return x ** y


print(my_func(2.0, -3))


# С помощью цикла

def my_func(x, y):
    if not isinstance(x, float) or x <= 0 or not isinstance(y, int) or y >= 0:
        print("x - неотрицательный float, y - отрицательный int")
        return

    d = x
    for i in range(1, abs(y)):
        d = d * x
    return 1 / d


print(my_func(2.0, -3))
