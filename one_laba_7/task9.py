# Скорость сборки одного робота (1 компьютер / 2 робота / 3 часа)
rate_per_robot = 1 / (2 * 3)

num_robots = 10

time = 12

computers_assembled = rate_per_robot * num_robots * time

# Вывод результата
print(f"10 роботов соберут {computers_assembled} компьютеров за 12 часов.")
