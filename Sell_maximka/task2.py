def second_hash(string):
    return len(string)

def third_hash(string):
    if string:
        return ord(string[0]) - ord('a') + 1
    return -1

def fourth_hash(string, size):
    prime_numbers = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    if string:
        hash_value = sum(prime_numbers.get(char, 1) for char in string.lower())
        return hash_value % size
    return -1

def create_phonebook():
    names = ["Estl1er", "Ben", "ВоЬ", "Dan"]
    for name in names:
        print("Name:", name)
        print("Second Hash:", second_hash(name))
        print("Third Hash:", third_hash(name))
        print("Fourth Hash:", fourth_hash(name, len(names)))
        print()

# Вызов функции для телефонной книги
create_phonebook()
