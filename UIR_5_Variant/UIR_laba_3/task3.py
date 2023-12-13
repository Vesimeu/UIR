battery_voltage = {
    'А': '1.5V',
    'АА': '1.5V',
    'ААА': '1.5V',
    'АААА': '9V'
}

def hash_function_5_6(battery_size, table_size=10):
    return len(battery_size) % table_size

for size, voltage in battery_voltage.items():
    hash_code = hash_function_5_6(size)
    print(f"Размер батарейки: {size}, Напряжение: {voltage}, Хеш-код: {hash_code}")
