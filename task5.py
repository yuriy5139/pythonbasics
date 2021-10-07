from functools import reduce
s_list = [item for item in range(100, 1001) if item %2 == 0]
print(reduce(lambda sum, item: sum+item, s_list))
