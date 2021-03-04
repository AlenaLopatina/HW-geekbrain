class Road:
    __asphalt = 25
    __dep = 0.05
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def massa(self):
        return self._length * self._width * self.__asphalt * self.__dep

r = Road(20, 500)
print(r.massa())