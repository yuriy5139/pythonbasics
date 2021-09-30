my_list = [9, 8, 8, 7, 6, 6, 6, 4, 3]

number = int(input("введите натуральное число "))
#Если список большой, лучше делать бинарный поиск, но здесь сделаем простой проход в else
if number in set(my_list):
    my_list.insert(my_list.index(number),number)
elif (number >= my_list[0]):
    my_list.insert(0, number)
elif (number <= my_list[-1]):
    my_list.append(number)
else:
    for pos, item in enumerate(my_list):
        if item <= number:
            my_list.insert(pos, number)
            break

print(my_list)