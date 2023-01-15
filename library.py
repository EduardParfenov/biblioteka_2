
class Library:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception('У данного класса может быть только один экземпляр.')

    def __init__(self, lib_name='Библиотека им. Маяковского'):
        self.lib_name = lib_name
        self.books = 459

    def __str__(self):
        return self.lib_name



# library = Library()
# print('Библиотека:')
# print(library)
# print()
# librarian1 = Librarian('Марь Иванна')
# librarian2 = Librarian('Евгения Барисовна')
# librarian3 = Librarian('Евдакинья Георгевна')
#
# print('Сотрудники:')
# for i in (librarian1, librarian2, librarian3):
#     print(i)
