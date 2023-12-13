import random


def mirror_matrix(matrix):
    n = len(matrix)

    # Создаем новую матрицу, заполняем ее нулями
    mirrored_matrix = [[0] * n for _ in range(n)]

    # Проходим по строкам и столбцам и заполняем новую матрицу
    for i in range(n):
        for j in range(n):
            mirrored_matrix[i][j] = matrix[i][n - j - 1]

    return mirrored_matrix


def generate_random_matrix(n):
    # Генерируем случайную матрицу размером NxN с числами от 0 до 9
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]


# Пользователь вводит N
N = int(input("Введите значение N (нечетное число): "))

# Генерируем случайную матрицу
original_matrix = generate_random_matrix(N)

# Выводим исходную матрицу
print("Исходная матрица:")
for row in original_matrix:
    print(" ".join(map(str, row)))

# Применяем функцию к матрице
mirrored_matrix = mirror_matrix(original_matrix)

# Выводим результат
print("\nОтраженная матрица:")
for row in mirrored_matrix:
    print(" ".join(map(str, row)))
