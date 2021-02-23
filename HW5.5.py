def summary():
    try:
        with open('hw5.txt', 'w+') as file_hw5:
            line = input('Введите цифры через пробел \n')
            file_hw5.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except ValueError:
        print('Ошибка ввода')
summary()