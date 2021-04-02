class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    def get_surname(self):
        surname_a = self._surname
        return surname_a


x = Person('Anna', 'Acco', 25)
print(x.name)
print(x.get_surname())
print(x.__age)
