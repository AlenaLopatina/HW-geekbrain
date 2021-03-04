class Worker:
    def __info__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = wage
        self._bonus = bonus

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._wage + self._bonus


worker = Position("Alena", "Lopatina", "Manager", 4000, 1000)

print(worker.get_full_name())
print(worker.get_total_income())
