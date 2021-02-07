my_list = [7, 5, 3, 3, 2]
print("Рейтинг :", my_list)
posl = len(my_list)
element = int(input("Введите, пожалуйста,новый элемент"))
for el in range(len(my_list)):
    if my_list[el] == element:
        my_list.insert(el + 1, element)
        break
    elif my_list[0] < element:
        my_list.insert(0, element)
        break
    elif my_list[posl-1] > element:
        my_list.append(element)
        break
    elif my_list[el] > element > my_list[el + 1]:
        my_list.insert(el + 1, element)
        break
print("Новый рейтинг", my_list)

