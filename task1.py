def divide():
    """Divides two numbers from user input"""
    try:
        a = float(input("введите число a "))
        b = float(input("введите число b "))
        c = a / b
        print("Ответ: ", c)
    except ValueError:
        print("Допустим ввод только числовых аргументов")
    except ZeroDivisionError:
        print("Деление на 0 в этой версии не поддерживается")

divide()