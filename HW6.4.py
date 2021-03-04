class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print('Завести машину')

    def stop(self):
        return print('Выключить мотор')

    def turn(self, direction):
        return print(f'Поварачивает {direction}')

    def show_speed(self):
        return print(f"Текущая скорость", self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!' + str(self.speed)
        return str(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!! ' + str(self.speed)
        return str(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


mazerati = SportCar(200, 'Red', 'Mazerati', False)
toyta = TownCar(60, 'Black', 'Toyta', False)
kia = WorkCar(70, 'Yellow', 'Kia', False)
avtovaz = PoliceCar(120, 'White', 'Avtovaz', True)
print(mazerati.turn(direction='налево'))
print(f'{avtovaz.name} цвет {avtovaz.color}')
print(kia.show_speed())

