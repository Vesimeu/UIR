# Гравитационная постоянная (в м^3/(кг*с^2))
G = 6.67430e-11

# Запрос массы и расстояния от пользователя
m1 = float(input("Введите массу первого тела (кг): "))
m2 = float(input("Введите массу второго тела (кг): "))
r = float(input("Введите расстояние между телами (м): "))

# Вычисление силы притяжения
F = (G * m1 * m2) / (r ** 2)

print(f"Сила притяжения между телами: {F} Ньютона")
