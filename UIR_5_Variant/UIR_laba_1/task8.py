# Ввод скорости лодки в стоячей воде, скорости течения реки и время движения
V = float(input("Введите скорость лодки в стоячей воде (км/ч): "))
U = float(input("Введите скорость течения реки (км/ч): "))
T1 = float(input("Введите время движения по озеру (часы): "))
T2 = float(input("Введите время движения по реке против течения (часы): "))

# Вычисление пути, пройденного лодкой
distance_lake = V * T1
distance_river = (V - U) * T2

total_distance = distance_lake + distance_river

# Вывод результата с точностью до 4 цифр в дробной части
print(f"Путь, пройденный лодкой: {total_distance:.4f} км")
