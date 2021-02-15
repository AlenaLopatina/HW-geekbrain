from sys import argv

salary2, hours, rate, bonus = argv

print("Имя скрипта: ", salary2)
print("Выработка в часах: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", bonus)


def salary(hours, rate, bonus):
    """Возващает зарплату сотрудника"""
    return hours * rate + bonus
print(salary())


print(salary())
