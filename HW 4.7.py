def fact(n):
    temp = 1
    for el in range(1, n + 1):
        temp = el * temp
        yield temp


n = int(input("Введите число"))

x = 0
for i in fact(n):
    if x < 15:
        print(i)
        x = x + 1
    else:
        break
