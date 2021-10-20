import re


class NotIntException(BaseException):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []
while True:
    try:
        nextnum = input("введите число для добавления в список ")
        if nextnum == "stop":
            break
        if not re.match(r'\d+', nextnum):
            raise NotIntException("Ошибка! В список можно вносить только целые числа!")
        my_list.append(int(nextnum))
    except BaseException as e:
        print(e)

print("Результирующий список:", my_list)
