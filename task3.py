from pathlib import Path

fname = 'task3.txt'
Path(fname).touch()  # как будто создали непрограммно, чтобы не тянуть в git текстовые файлы

salary = {
    'Корейко': 10000000,
    'Бендер': 1000000,
    'Балаганов': 5000,
    'Паниковский': 2500,
    'Козлевич': 1000
}

try:
    with open(fname, 'w', encoding='utf8') as f:
        for dude, money in salary.items():
            print(dude, money, file=f)
except Exception as e:
    print("что-то пошло не так: ", e)

try:
    with open(fname, 'r', encoding='utf8') as f:
        total = []
        for ln in f:
            total.append(int(ln.split(' ')[1]))
            if int(ln.split(' ')[1]) < 20000:
                print("У сотрудника {} оклад меньше 20000!".format(ln.split(' ')[0]))
    print("Cредний оклад = ", sum(total) / len(total))
except Exception as e:
    print("что-то пошло не так: ", e)
