def int_func(text):
    all_text = []
    for i in range(len(text)):
        all_text.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(all_text)


def inf_func_2():
    print(int_func(input('Введите пару слов: ').split()))


inf_func_2()
