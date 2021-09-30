num = int(input("Сколько будет товаров? "))
goods = []
for i in range(num):
    print("введите характеристики товара", i + 1)
    name = input("название: ")
    price = int(input("цена: "))
    qty = int(input("количество: "))
    ei = input("единицы измерения: ")
    goods.append((i + 1, {"название": name, "цена": price, "количество": qty, "ед": ei}))

print(goods)

summary = {}
for (id, good) in goods:
    for key, val in good.items():
        if key in summary:
            if not (val in summary[key]):
                summary[key].append(val)
        else:
            summary[key] = []
            summary[key].append(val)
print(summary)
