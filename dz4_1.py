# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
import numpy as np

def matrix_transpose(mx: list) -> list:
    matrix = np.array(mx)
    return list(matrix.transpose())


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.transpose())
