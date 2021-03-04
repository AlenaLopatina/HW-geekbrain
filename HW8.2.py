class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Введите делимое: '))
    division = int(input('Введите делитель: '))
    if not division:
        raise Zero('Нельзя делить на ноль')
    print(f'Результат {devidend/division}')

except ValueError:
    print('Вы ввели не числа')
except Zero as error:
    print(error)