def my_func(a, b, c, ):
    """Возвращает сумму 2х наибольших элементов"""
    summa = 0
    if a >= c and b >= c:
        summa = a + b
    elif b < a < c:
        summa = a + c
    else:
        summa = b + c
    return summa


print("Сумма 2х максимальных элементов:",
      my_func(int(input("Введите 1 элемент")), int(input("Введите 2 элемент")), int(input("Введите 3 элемент"))))
