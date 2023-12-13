import hashlib

book_authors = {
    'Maus': 'Art Spiegelman',
    'Fun Home': 'Alison Bechdel',
    'Watchmen': 'Alan Moore'
}

def hash_function_5_7(book_name, table_size=10):
    hash_object = hashlib.md5(book_name.encode())
    hash_hex = int(hash_object.hexdigest(), 16)
    return hash_hex % table_size

for book, author in book_authors.items():
    hash_code = hash_function_5_7(book)
    print(f"Название книги: {book}, Автор: {author}, Хеш-код: {hash_code}")
