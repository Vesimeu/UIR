import hashlib

phone_book = {
    'Estl1er': '555-1111',
    'Ben': '555-2222',
    'ВоЬ': '555-3333',
    'Dan': '555-4444'
}

def hash_function_5_5(name, table_size):
    hash_object = hashlib.md5(name.encode())
    hash_hex = int(hash_object.hexdigest(),16)
    return hash_hex % table_size


for name, phone in phone_book.items():
    hash_code = hash_function_5_5(name, table_size=10)
    print(f"Имя: {name}, Номер телефона: {phone}, Хеш-код: {hash_code}")
