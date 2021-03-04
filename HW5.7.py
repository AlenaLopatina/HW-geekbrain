import json

result = []
profit = {}
average = []

with open("company_info.txt", 'r', encoding='utf-8') as com_info:
    counter = 1
    while True:
        line = com_info.readline().split()

        if not line:
            break

        profit[line[0]] = int(line[-2]) - int(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1

result = [profit, {'average_profit': sum(average) / len(average)}]

with open("company_info_new", 'w', encoding='utf-8') as file_new:
    json.dump(result, file_new)
