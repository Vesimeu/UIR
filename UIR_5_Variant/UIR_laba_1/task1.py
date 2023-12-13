import math
def func_a(x,y):
    return (2*math.cos(x - math.pi/6)**4)/((1/2) + math.sin(y)**2)
def func_b(z):
    return (1 + (z**2)/(3 + z**2/5))

def main():
    x  = float(input("Введите x" + "\n"))
    y = float(input("Введите x"+ "\n"))
    z = float(input("Введите x"+ "\n"))

    print("Функция a = " + str(func_a(x,y)))
    print("Функция b = " + str(func_b(z)))


if __name__ == "__main__":
    main()