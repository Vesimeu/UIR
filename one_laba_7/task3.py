import math


def func(x):
    f_x = math.log10(x**2 + 1) + 1,25 * x
    return f_x

h = 0.1
x = 1
while x<(3+h):
    print("Функция f(x) = " + str(func(x)) + "при x = " + str(x))
    x = x+h
