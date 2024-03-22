import numpy as np

class HashMixin:
    def __hash__(self):
        # Сумма всех элементов матрицы по модулю 100
        return hash(np.sum(self.array) % 100)

class AdvancedMatrix(HashMixin):  # Наследуем от HashMixin
    def __init__(self, array):
        self.array = np.array(array)

    def __eq__(self, other):
        # Сравнение матриц на равенство
        return np.array_equal(self.array, other.array)

    def __matmul__(self, other):
        # Матричное умножение
        return AdvancedMatrix(self.array @ other.array)
        
class AdvancedMatrix:
    def __init__(self, array):
        self.array = np.array(array)

    def __eq__(self, other):
        return np.array_equal(self.array, other.array)

    def __hash__(self):
        return hash(np.sum(self.array) % 100)

    def __matmul__(self, other):
        return AdvancedMatrix(self.array @ other.array)


# Генерация матриц
np.random.seed(0)
A = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))
B = AdvancedMatrix(np.random.randint(0, 10, (10, 10)))
C = AdvancedMatrix(A.array.copy())
C.array[0,0] += 1
C.array[1,0] -= 1
D = B

# Проверки
assert A != C, "A and C should not be equal as matrices"
assert B == D, "B and D should be equal"
assert not np.array_equal((A @ B).array, (C @ D).array), "(A @ B) and (C @ D) should not be equal"
assert hash(A) == hash(C), "Hashes of A and C should be equal"  # Это проверка того, что вызывает коллизию хеша


# Сохраняем матрицы и результаты в файлы
for matrix, name in zip([A, B, C, D], ['A', 'B', 'C', 'D']):
    np.savetxt(f'{name}.txt', matrix.array, fmt='%d')

# Выполняем матричное умножение
AB = A @ B
CD = C @ D

# Сохраняем результаты произведений
np.savetxt('AB.txt', AB.array, fmt='%d')
np.savetxt('CD.txt', CD.array, fmt='%d')

# Сохраняем хэши матриц AB и CD в файл
with open('hash.txt', 'w') as f:
    f.write(f'Hash of AB: {hash(AB)}\n')
    f.write(f'Hash of CD: {hash(CD)}\n')
