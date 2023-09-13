# Задача 3. Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class MyException(Exception):
    pass


class MyExceptionNotEqualNumberMatrixRows(MyException):
    def __init__(self, matrix_first, matrix_second):
        self.matrix_first = matrix_first
        self.matrix_second = matrix_second

    def __str__(self):
        return (f'Количество строк 1-матрицы: {self.matrix_first.get_number_rows()} '
                f'должна равняться количеству строк 2-матрицы:{self.matrix_second.get_number_rows()}')


class MyExceptionNotEqualMatrixColumns(MyException):
    def __init__(self, matrix_first: list[list[int]], matrix_second: list[list[int]]):
        self.matrix_first = matrix_first
        self.matrix_second = matrix_second

    def __str__(self):
        return (f'Количество столбцов 1-матрицы {m1.get_number_columns()} '
                f'должна равняться количеству столбцов 2-матрицы:{m2.get_number_columns()}')


class Matrix:
    def __init__(self, mt: list[list[int]]):
        self.mt = mt

    def get_number_rows(self):
        return len(self.mt)

    def get_number_columns(self):
        return len(self.mt[0])

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
    print(m1)
    print(m2)

    if m1.get_number_rows() != m2.get_number_rows():
        raise MyExceptionNotEqualNumberMatrixRows(m1, m2)
    print(m1 + m2)

    m6 = Matrix([[1, 1, 1], [1, 1, 1]])
    print(m6)
    # print(m1.get_number_rows(),m6.get_number_rows())
    if m1.get_number_rows() != m6.get_number_rows():
        raise MyExceptionNotEqualNumberMatrixRows(m1, m6)
    print(m1 + m6)
