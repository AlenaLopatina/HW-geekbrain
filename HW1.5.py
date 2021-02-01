gain = int(input('Введите выручку компании в рублях'))
costs = int(input('Введите издержки компании в рублях'))
if gain > costs:
    print("У Вас прибыль, Ваша рентабельность :", (gain - costs) / costs)
    people = int(input('Введите количество сотрудников'))
    print('Прибыль на 1 сотрудника:', (gain - costs) / people)
else:
    print('У Вас убыток')
