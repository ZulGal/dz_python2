# Задача 3. Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц


class Matrix:
    def __init__(self, mt: list[list[int]]):
        self.mt = mt

    def __str__(self):
        res = ''
        for row in self.mt:
            for element in row:
                res += f'{element} '
            res += '\n'
        return (res)

    def __add__(self, other: "Matrix"):
        return Matrix([[element1 + element2 \
                        for element1, element2 in zip(row1, row2)] \
                        for row1, row2 in zip(self.mt, other.mt)])

    def __mul__(self, other: "Matrix"):
        length = len(self.mt)
        result_mt = [[0 for i in range(length)] for i in range(length)]
        return [[sum(self.mt[i][n] * other.mt[n][j] \
                    for n in range(length)) \
                    for j in range(length)] for i in range(length)]

    def __eq__(self, other: "Matrix"):
        for i in range(len(self.mt)):
            for j in range(len(self.mt[i])):
                if self.mt[i][j] != other.mt[i][j]:
                    return False
        return True


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m4 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 == m2)
    print(m1 == m3)
    print(m1 * m4)
