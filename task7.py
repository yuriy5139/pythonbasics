import json
import random
import re

opf = ['ООО', 'ПАО', 'ЗАО']
name1 = ['Альфа', 'Бета', 'Гамма', 'Дельта']
name2 = ['Консалтинг', 'Инициатива', 'Мануфэкчуринг', 'Проект']
name3 = ['Липецк', 'Воронеж', 'Сызрань', 'Грязовец', 'Тегусигальпа']

fname = 'task7.txt'
json_file = 'task7.json'


def fake_company():
    return f'{random.choice(opf)} \"{random.choice(name1)} {random.choice(name2)} {random.choice(name3)}\" {random.randint(1000, 1000000)} {random.randint(1000, 1000000)}'


with open(fname, 'w', encoding='utf16') as f:
    usednames = set()  # для проверки, что не генерируем одинаковые имена
    for i in range(10):
        info = fake_company()
        if info.split("\"")[1] in usednames:
            continue
        else:
            usednames.add(info.split("\"")[1])
            print(info, file=f)


def corp_result(ln):
    m = re.search(r'(\d+) (\d+)', ln)
    return int(m.group(1)) - int(m.group(2))


profits = []
companies = {}

with open(fname, 'r', encoding='utf16') as f:
    for ln in f:
        result = corp_result(ln)
        companies[ln.split("\"")[1]] = result
        if result > 0:
            profits.append(result)

average_profit = {'average_profit': sum(profits) / len(profits)}

with open(json_file, 'w', encoding='utf16') as f:
    json.dump([companies, average_profit], f)
