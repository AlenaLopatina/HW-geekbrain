sentence = input("Введите, пожалуйста, пару слов")
sentence1 = sentence.split()
for ind, el in enumerate(sentence1, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[0:10])
