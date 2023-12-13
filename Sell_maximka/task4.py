def second_hash(string):
    return len(string)

def third_hash(string):
    if string:
        return ord(string[0]) - ord('A') + 1
    return -1

def fourth_hash(string, size):
    prime_numbers = {'Maus': 2, 'Fun Home': 3, 'Watchmen': 5}
    if string in prime_numbers:
        return prime_numbers[string] % size
    return -1

def create_book_author_map():
    books = {"Maus": "Art Spiegelman", "Fun Home": "Alison Bechdel", "Watchmen": "Alan Moore"}
    for title in books:
        print("Title:", title)
        print("Second Hash:", second_hash(title))
        print("Third Hash:", third_hash(title))
        print("Fourth Hash:", fourth_hash(title, len(books)))
        print()

# Вызов функции для соответствия книг и авторов
create_book_author_map()
