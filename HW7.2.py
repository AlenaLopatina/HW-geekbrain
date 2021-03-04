class Clothes:

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'


    def abstract(self):
        return 'Стильная одежда'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Стильное пальто'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Стильный костюм'


coat = Coat(100)
costume = Costume(10)
print(coat.consumption())
print(costume.consumption())
print(coat.abstract())
print(costume.abstract())