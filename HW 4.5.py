from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(f'Четные числа от 100 до 1000 {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат произведения всех четных чисел {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

