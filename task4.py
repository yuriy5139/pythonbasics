user_input = input("введите слова, разделенные пробелами ")
for i, word in enumerate(user_input.split()):
    print(i, word[:10])