
class Librarian:
    __instance = None
    __instance_amount = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None or cls.__instance_amount < 3:
            cls.__instance = super().__new__(cls)
            cls.__instance_amount += 1
            return cls.__instance
        else:
            raise Exception('У данного класса может быть только три экземпляра.')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name