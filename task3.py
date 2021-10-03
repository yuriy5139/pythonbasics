def my_func(a, b, c):
    return sum(sorted(list([a, b, c]))[-2:])


print(my_func(5, 6, 7))
