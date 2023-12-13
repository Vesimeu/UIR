import math

# Ускорение свободного падения
g = 9.81  # м/с²

# Высота H (в метрах)
H = float(input("Введите высоту H (в метрах): "))

# Начальная скорость V (в м/с)
V = float(input("Введите начальную скорость V (в м/с): "))

# Вычисление времени падения
discriminant = V**2 - 2 * g * H

# Проверка, можно ли вычислить время
if discriminant >= 0:
    t1 = (-V - math.sqrt(discriminant)) / -g
    t2 = (-V + math.sqrt(discriminant)) / -g

    # Время падения (берем только отрицательное значение, если оно существует)
    if t1 >= 0:
        time_of_fall = t1
    else:
        time_of_fall = t2

    print(f"Время падения: {time_of_fall:.2f} секунд")
else:
    print("Тело не достигнет заданной высоты.")

