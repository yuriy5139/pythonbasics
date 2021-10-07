s_list = [300, 12, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list((item for i, item in enumerate(s_list[1:], start=1) if item > s_list[i - 1])))
