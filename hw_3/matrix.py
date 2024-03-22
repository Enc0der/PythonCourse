import numpy as np

# Определение класса матрицы
class Matrix:
    def __init__(self, array):
        # Инициализация матрицы
        if isinstance(array, np.ndarray):
            self.matrix = array
        else:
            raise ValueError("Input should be a NumPy ndarray")

    def __add__(self, other):
        # Перегрузка оператора сложения
        if self.matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must be of the same size")
        return Matrix(self.matrix + other.matrix)

    def __mul__(self, other):
        # Перегрузка оператора покомпонентного умножения
        if self.matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must be of the same size for element-wise multiplication")
        return Matrix(self.matrix * other.matrix)

    def __matmul__(self, other):
        # Перегрузка оператора матричного умножения
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError("Matrices are not aligned for dot product")
        return Matrix(self.matrix @ other.matrix)

# Установка seed для воспроизводимости
np.random.seed(0)

# Генерация двух матриц
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Выполнение операций
matrix_sum = matrix1 + matrix2
matrix_elementwise_mul = matrix1 * matrix2
matrix_dot_mul = matrix1 @ matrix2

# Запись результатов в файлы
with open('matrix+.txt', 'w') as f:
    f.write(np.array_str(matrix_sum.matrix))

with open('matrix*.txt', 'w') as f:
    f.write(np.array_str(matrix_elementwise_mul.matrix))

with open('matrix@.txt', 'w') as f:
    f.write(np.array_str(matrix_dot_mul.matrix))

