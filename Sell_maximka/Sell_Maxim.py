def first_hash(string):
    return 1

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

def main():
    string = "bag"

    print("First Hash:", first_hash(string))
    print("Second Hash:", second_hash(string))
    print("Third Hash:", third_hash(string))
    size = 10  # Размер хеша
    print("Fourth Hash:", fourth_hash(string, size))

# Вызов главной функции
main()
