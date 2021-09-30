my_list = input("Введите элементы списка через запятую ").split(',')

for i in range(0, len(my_list) - 1 if len(my_list) % 2 else len(my_list), 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)