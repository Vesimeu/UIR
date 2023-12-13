import math
def func(x):
    return math.tan(abs(math.log(x**2,math.exp(1))))**2

for i in range(10,31,1):
    print("Функция F(x) = " + str(func(i/10)) + " при x = " + str(i/10))