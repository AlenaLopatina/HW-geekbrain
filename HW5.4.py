dic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

with open('number.txt', 'r', encoding='utf-8') as number_read:
    lines = number_read.readlines()

with open('number_rus', 'a', encoding='utf-8') as number_write:
    for line in lines:
        row = line.split()
        row[0] = dic[row[0]]
        print(' '.join(row), file=number_write)
