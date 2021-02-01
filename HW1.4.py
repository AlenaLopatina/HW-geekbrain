number = int(input('Введите целое положительное число'))
maxi = number % 10
number = number // 10
while number > 0:
    if number % 10 > maxi:
        maxi = number % 10
    number = number // 10
print('Самая большая цифра в числе', maxi)
