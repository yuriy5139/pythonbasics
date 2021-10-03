def listsum():
    print("Для заверщения работы используйте символ ;")
    result = 0
    while True:
        line = input("введите числа, разделенные запятыми ")
        result += sum(map(lambda item: int(item) if len(item) else 0, line.split(';')[0].split(',')))
        if len(line.split(';')) > 1:
            return result


print(listsum())
