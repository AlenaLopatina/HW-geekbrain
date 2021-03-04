from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

my_list = [2, "Мама", True, 10, 25]
c = 0
for el in cycle(my_list):
    if c >= len(my_list):
        break
    print(el)
    c = c + 1
