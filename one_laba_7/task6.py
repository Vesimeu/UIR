import math

R = int(input("Введите радиус R (1 <= R <= 100): "))

# Проверка
if 1 <= R <= 100:

    circumference = 2 * math.pi * R


    area = math.pi * R**2

    print(f"Длина окружности: {circumference:.4f}")
    print(f"Площадь круга: {area:.4f}")
else:
    print("Значение R должно быть в диапазоне от 1 до 100.")
