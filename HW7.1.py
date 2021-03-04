class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for y in range(len(other.my_list[i])):
                self.my_list[i][y] = self.my_list[i][y] + other.my_list[i][y]
        return Matrix.__str__(self)


matrix = Matrix([[1, 0, 1], [1, 0, 1], [1, 1, 1]])
new_matrix = Matrix([[2, 2, 2], [1, 1, 1], [3, 3, 3]])
print(matrix.__add__(new_matrix))