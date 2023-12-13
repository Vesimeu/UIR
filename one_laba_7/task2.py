
def func(x):
    c = 2
    b = -1
    f_x = (c*x**2 + x)/(b*x**2) + (x)**(2/3)
    return f_x

h = 0.1
x=1
while (x < (2 + h)):
    print("Функция F(x) = " + str(func(x)) + "при x = " + str(round(x,3)))
    x = x + h
