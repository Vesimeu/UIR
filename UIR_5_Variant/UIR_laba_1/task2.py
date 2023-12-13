import math
def func(x):
    a = 2
    b = 1
    c = -1
    return math.sqrt(((x**2 + a*x)/b) + c * x**2)
h = 0.05
x = 2

for i in range(200,210,5):
    print("Функция F(x) = " + str(func(i/100)) + " при x = " + str(i/100))