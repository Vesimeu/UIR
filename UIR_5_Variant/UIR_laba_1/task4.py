import math

# Функция для вычисления площади треугольника по его сторонам (формула Герона)
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Функция для вычисления радиуса вписанной окружности в треугольник
def calculate_incircle_radius(a, b, c):
    area = calculate_area(a, b, c)
    return 2 * area / (a + b + c)

# Запрос координат вершин треугольника от пользователя
x1, y1 = map(float, input("Введите координаты вершины 1 (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты вершины 2 (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты вершины 3 (x3 y3): ").split())

# Вычисление длин сторон треугольника
side_a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
side_b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
side_c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Вычисление радиуса вписанной окружности
incircle_radius = calculate_incircle_radius(side_a, side_b, side_c)

print(f"Радиус вписанной окружности в треугольник: {incircle_radius}")
