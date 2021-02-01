time = int(input('введите время в секундах'))
a = time // 3600
b = (time - a * 3600) // 60
c = time - a * 3600 - b * 60
print("%02d:%02d:%02d" % (a, b, c))
