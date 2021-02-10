def my_func():
    """Возващает сумму чисел"""

    summa = 0
    number = input('Введите числа через пробел или X для выхода').split()
    for el in number:

        if el == "X":
            print("Сумма", summa)
            return
        else:
            summa = summa + int(el)
    print("Сумма", summa)


my_func()
