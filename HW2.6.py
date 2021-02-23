goods = int(input("Введите кол-во товаров "))
i = 1
goods_list = []
goods_dict = []
goods_analytics = {}
while i <= goods:
    goods_dict = dict({"название": input("Введите название товара"), "цена": input("Введите цену товара"),
                       "количество": input('Введите кол-во товара'), "eд": input("Введите единицу измерения ")})
    goods_list.append((i, goods_dict))
    i = i + 1
for el in goods_list:
    print(el)
for key in goods_dict.keys():
    analytic_list = []
    for el in goods_list:
        analytic_list.append(el[1][key])
        goods_analytics[key] = analytic_list
print("Аналитика",goods_analytics)
