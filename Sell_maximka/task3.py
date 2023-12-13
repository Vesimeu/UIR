def second_hash(string):
    return len(string)

def third_hash(string):
    if string:
        return ord(string[0]) - ord('A') + 1
    return -1

def fourth_hash(string, size):
    prime_numbers = {'A': 2, 'AA': 3, 'AAA': 5, 'AAAA': 7}
    if string in prime_numbers:
        return prime_numbers[string] % size
    return -1

def create_battery_voltage_table():
    battery_sizes = ["A", "AA", "AAA", "AAAA"]
    for size in battery_sizes:
        print("Size:", size)
        print("Second Hash:", second_hash(size))
        print("Third Hash:", third_hash(size))
        print("Fourth Hash:", fourth_hash(size, len(battery_sizes)))
        print()

# Вызов функции для таблицы размеров батареек и напряжения
create_battery_voltage_table()
