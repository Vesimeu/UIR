import numpy as np

#  вектора a
ax = float(input("Введите координату ax: "))
ay = float(input("Введите координату ay: "))
az = float(input("Введите координату az: "))

# вектора b
bx = float(input("Введите координату bx: "))
by = float(input("Введите координату by: "))
bz = float(input("Введите координату bz: "))

#  вектора c
cx = float(input("Введите координату cx: "))
cy = float(input("Введите координату cy: "))
cz = float(input("Введите координату cz: "))

# Создание
a = np.array([ax, ay, az])
b = np.array([bx, by, bz])
c = np.array([cx, cy, cz])

# Вычисление
cross_product_ab = np.cross(a, b)

# Модуль векторного произведения
area = np.linalg.norm(cross_product_ab)

# Площадь боковой поверхности параллелепипеда
print(f"Площадь боковой поверхности параллелепипеда: {area:.2f}")
