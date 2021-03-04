file = open("hw.txt", "r")
content = file.readlines()

print(f' Строк {len(content)}')

i = 1
for str in content:
    print(f'В строке {i} {len(str.split())} слова')
    i = i + 1

file.close()
