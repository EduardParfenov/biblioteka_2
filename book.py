from abc import ABC, abstractmethod

class Books(ABC):
    def __init__(self):
        self.books_dict = dict()

    @abstractmethod
    def type_book(self):
        pass

    def add_book(self):
        new_book = input('Введите название книги ')
        book_amount = input('Сколько копий? \n').strip()

        assert book_amount.isdigit(), 'Нужно ввести число'
        book_amount = int(book_amount)

        if new_book not in self.books_dict:
            self.books_dict[new_book] = book_amount
        else:
            self.books_dict[new_book] += book_amount

    def __getitem__(self, item):
        return self.books_dict[item]

    def __str__(self):
        return ''.join(f'Название книги: {key}, количество: {value}\n' for key, value in self.books_dict.items())

class Fantasy(Books):
    def type_book(self):
        return 'Фэнтези'

class Roman(Books):
    def type_book(self):
        return 'Романы'

class Horror(Books):
    def type_book(self):
        return 'Ужасы'


# new_factory = BookFactory()
# book1 = new_factory.create_book()
# book2 = new_factory.create_book()
# book3 = new_factory.create_book()
# new_factory.check_books()