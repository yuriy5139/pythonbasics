from pathlib import Path
import random


def randombla(words=5, letters=8):
    ln = ""
    for i in range(words):
        ln += "".join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(1, letters))) + " "
    return ln


fname = 'task2.txt'
Path(fname).touch()  # как будто создали непрограммно, чтобы не тянуть в git текстовые файлы

try:
    with open(fname, 'a', encoding='utf8') as f:
        for i in range(random.randint(1, 10)):
            print(randombla(words=random.randint(1, 8)), file=f)
except FileNotFoundError:
    print("файл не найден, попробуйте раскомментировать touch в строке 13")

try:
    with open(fname, 'r', encoding='utf8') as f:
        for i, line in enumerate(f):
            print("Слов в строке {}: {}".format(i + 1, len(line.split(" ")) - 1))
except Exception as e:
    print("что-то пошло не так: ", e)
