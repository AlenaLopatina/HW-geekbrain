class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


result_list = []
while True:
    value = input('Введите число или stop для выхода: ')

    if value == 'stop':
        print(f'Текущий список {result_list}')
        break

    try:
        if not value.isnumeric():
            raise NotANumberException('Не число!')
        result_list.append(int(value))
    except NotANumberException as error:
        print('Вы ввели не число')