def division_func():
    """Возвращает частное от деления.

        параметры:
        p_1 -- делимое
        p_2 -- делитель

     """
    try:
        p_1 = float(input("Введите делимое: "))
        p_2 = float(input("Введите делитель: "))
    except ValueError:
        return
    if p_2 == 0:
        return print("Нельзя делить на ноль")
    return p_1 / p_2


div = division_func()
print("Результат деления :", div)
