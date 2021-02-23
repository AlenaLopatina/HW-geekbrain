with open('file.txt', 'w') as file:
    while True:
        line = input('Введите текст \n')
        if not line:
            break
        file.write(f'{line}\n')
