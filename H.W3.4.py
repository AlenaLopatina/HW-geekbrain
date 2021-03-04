def my_func_1(x, y):
    """возведение числа x в степень y"""
    return x ** y


print("x в степени y", my_func_1(int(input("Введите положительное x")), int(input("Введите отрицательное  y"))))

def my_func_2(x, y):
    """возведение числа x в степень y"""
    extent =1
    for i in range(abs(y)):
        extent = extent*x

    return 1/extent


print("x в степени y", my_func_2(int(input("Введите положительное x")), int(input("Введите отрицательное  y"))))

