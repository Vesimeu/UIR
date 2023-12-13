import hashlib

def hash_function_1(input_str, table_size):
    return 1


def hash_function_2(input_str, table_size):
    return len(input_str) % table_size


def hash_function_3(input_str, table_size):
    first_char = input_str[0].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(first_char) % table_size


def hash_function_4(input_str, table_size):
    letter_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
                       'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
                       'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}

    total = sum(letter_to_prime.get(char, 0) for char in input_str.lower())
    return total % table_size



input_str = "Minecraft"
table_size = 10

hash_code_1 = hash_function_1(input_str, table_size)
hash_code_2 = hash_function_2(input_str, table_size)
hash_code_3 = hash_function_3(input_str, table_size)
hash_code_4 = hash_function_4(input_str, table_size)
print("Слово которые хэшируется: " + input_str)
print(f"Хеш-код функции 1: {hash_code_1}")
print(f"Хеш-код функции 2: {hash_code_2}")
print(f"Хеш-код функции 3: {hash_code_3}")
print(f"Хеш-код функции 4: {hash_code_4}")


