from itertools import count, cycle, takewhile

#Задача 6.1

print(*takewhile(lambda num: num < 20, count(start=3)))

#Задача 6.2

print(*(el[1] for el in takewhile(lambda item: item[0] < 20, enumerate(cycle("ABCD"))))) # извините :)