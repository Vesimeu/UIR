import math

x = float(input("Введите x" + "\n"))
y = float(input("Введите y" + "\n"))
z = float(input("Введите z" + "\n"))

a = ((1 + math.sin(x+y)**2)/(2 + abs(x - (2*x)/(1 + x**2 * y**2)))) + x
b= math.cos(math.atan(1/z))**2

print("Функция a = " + str(a))
print("Функция b = " + str(b))