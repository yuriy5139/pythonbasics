import random

with open('task5.txt', 'w', encoding='utf8') as f:
    print(" ".join(random.sample("0123456789", random.randint(1, 10))), file=f)

with open('task5.txt', 'r', encoding='utf8') as f:
    ln = f.readline()
    if ln[-1] == '\n':
        ln = ln[:-1]
    print("Сумма элементов {} равна {}".format(ln, sum(map(int, ln.split(" ")))))
