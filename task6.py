import random
import re

topic = ["Информатика", "Физика", "Физкультура", "Природоведение", "ОБЖ", "Рисование", "Теорвер"]
fname = 'task6.txt'


def load():
    """
    задаем случайную нагрузку по предметам,
    и иногда (когда число не делится на 2 и не делится на 3),
    считаем, что часов по предмету нет
    """
    return list(map(lambda a: a if not a % 2 or a % 3 else 0, [random.randint(10, 100) for i in range(3)]))


with open(fname, 'w', encoding='utf16') as f:
    for t in topic:
        print(t, file=f, end=': ')
        for h, flavour in zip(load(), ["(л)", "(пр)", "(лаб)"]):
            print('{}{}'.format(h, flavour), file=f, end=' ') if h > 0 else print("—", file=f, end=' ')
        f.write('\n')

study = {}
with open(fname, 'r', encoding='utf16') as f:
    for ln in f:
        study[ln.split(': ')[0]] = sum(map(int, re.findall(r'(\d+)\(', ln.split(': ')[1])))

print(study)
