import numpy as np

# Mixin для арифметических операций
class ArithmeticMixin:
    def __add__(self, other):
        return self.__class__(self.array + other.array)
    
    def __sub__(self, other):
        return self.__class__(self.array - other.array)
    
    def __mul__(self, other):
        return self.__class__(self.array * other.array)
    
    def __truediv__(self, other):
        return self.__class__(self.array / other.array)

# Mixin для операций с файлами
class FileOperationsMixin:
    def write_to_file(self, filename):
        np.savetxt(filename, self.array, fmt='%d')
    
    @classmethod
    def read_from_file(cls, filename):
        array = np.loadtxt(filename, dtype=int)
        return cls(array)

# Mixin для отображения объекта
class DisplayMixin:
    def __str__(self):
        return np.array2string(self.array, separator=', ')

# Mixin для геттеров и сеттеров
class AccessMixin:
    @property
    def array(self):
        return self._array
    
    @array.setter
    def array(self, value):
        self._array = np.array(value, dtype=int)

# Основной класс, сочетающий все примеси
class AdvancedMatrix(ArithmeticMixin, FileOperationsMixin, DisplayMixin, AccessMixin):
    def __init__(self, array):
        self.array = array  # Использование сеттера из AccessMixin

# Использование класса
np.random.seed(0)
matrix1 = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))
matrix2 = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))

# Пример использования и сохранения результатов операций
matrix_sum = matrix1 + matrix2
matrix_diff = matrix1 - matrix2
matrix_prod = matrix1 * matrix2
matrix_quot = matrix1 / matrix2

# Сохранение результатов в файлы
matrix_sum.write_to_file('advanced_matrix+.txt')
matrix_diff.write_to_file('advanced_matrix-.txt')
matrix_prod.write_to_file('advanced_matrix*.txt')
matrix_quot.write_to_file('advanced_matrix_div.txt')

