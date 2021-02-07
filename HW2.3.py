month = int(input("Введите, пожалуйста, номер месяца"))
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
fall_list = [9, 10, 11]
season_dict = {"winter": "Зима", "spring": "Весна", "summer": "Лето", "fall": "Осень"}
if month in winter_list:
    print(season_dict.get("winter"))
elif month in spring_list:
    print(season_dict.get("spring"))
elif month in summer_list:
    print(season_dict.get("summer"))
else:
    print(season_dict.get("fall"))
