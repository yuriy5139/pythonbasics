s_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# решение с OrderedDict
def o_d_solution():
    from collections import OrderedDict
    d_list = []
    count_dict = OrderedDict()

    for key in s_list:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1

    for k, v in count_dict.items():
        if v == 1: d_list.append(k)

    return d_list


# решение с Counter()
def cntr_solution():
    from collections import Counter
    c = Counter(s_list)
    return [item for item in c if c[item] == 1]


# решение с генератором

def gen_solution():
    def two_or_more(l, item):
        l.pop(l.index(item))
        try:
            l.index(item)
            return True
        except ValueError:
            return False

    return [item for item in s_list if not two_or_more(s_list.copy(), item)]


# *** basic test ***
print(o_d_solution())
print(cntr_solution())
print(gen_solution())

# *** timeit test ***
import numpy as np
import timeit

s_list = list(np.random.choice(range(1000000), size=1000, replace=True))

print("Время решения с OrderedDict:", timeit.timeit(o_d_solution, number=10))
print("Время решения с Counter:", timeit.timeit(cntr_solution, number=10))
print("Время решения с генератором и copy():", timeit.timeit(gen_solution, number=10))