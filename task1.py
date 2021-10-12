with open("task1.txt", "w", encoding="utf16") as f:
    while True:
        inp = input('введите ')
        if inp:
            print(inp, file=f)
        else:
            print("спасибо")
            break
