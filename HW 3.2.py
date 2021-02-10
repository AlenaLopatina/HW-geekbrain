name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
year = input("Введите Ваш год рожднения: ")
city = input("Введите Ваш город: ")
email = input("Введите Ваш email: ")
phone = input("Введите Ваш телефон: ")


def data_func(**kwargs):
    """Возвращает информацию о пользователе.

            параметры: имя, фамилия, год, город,почта, телефон

         """
    return kwargs


info = data_func(имя=name, фамилия=surname, год=year, город=city, почта=email, телефон=phone)

print(f'Персоанальная информация', info)
