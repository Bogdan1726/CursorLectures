# encapsulation
"""
Private. Приватные члены класса недоступны извне - с ними можно работать только внутри класса.
Public. Публичные методы наоборот - открыты для работы снаружи и, как правило, объявляются публичными сразу
по-умолчанию.
Protected. Доступ к защищенным ресурсам класса возможен только внутри этого класса и также внутри унаследованных от
него классов (иными словами, внутри классов-потомков). Больше никто доступа к ним не имеет
"""


class Person:

    def __init__(self, name, surname, age):
        self.name = name  # public
        self._surname = surname  # protected
        self.__age = age  # private

    def __get_surname(self):
        surname_a = self._surname
        return surname_a


x = Person('Anna', 'Acco', 25)
print(x.name)
print(x._surname)
print(x.__age)



