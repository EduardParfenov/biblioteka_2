from book import Fantasy, Horror, Roman

class BookFactory:
    def __init__(self):
        self.all_books = {'Романы': list(),
                          'Фэнтези': list(),
                          'Ужасы': list()}

    def create_book(self):
        current_books = {'Романы': Roman,
                         'Фэнтези': Fantasy,
                         'Ужасы': Horror}
        book_genre = input('Укажите жанр который вас интересует:\n').strip().title()
        if book_genre in current_books:
            new_book = current_books[book_genre]()
            new_book.add_book()
            books = self.all_books[book_genre]
            books.append(new_book)
            return new_book
        else:
            print('У нас нет такого жанра.')

    def check_books(self):
        for book_genre, books in self.all_books.items():
            print(f'{book_genre}\n'
                  f'{" ".join(map(str(books)))}')