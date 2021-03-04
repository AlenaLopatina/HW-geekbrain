class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return 'Запуск отрисовки', self.title

class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return 'Запуск отрисовки', self.title

class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return 'Запуск отрисовки',self.title


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())