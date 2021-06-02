"""
classmethod — это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван.
Следовательно, classmethod — это метод, который привязан к классу, а не к экземпляру класса.
"""


class Car:

    TOTAL_WHEEL = 4

    def __init__(self):
        Car.TOTAL_WHEEL = Car.TOTAL_WHEEL + 1

    @staticmethod
    def print():
        print('Hello')

    @classmethod
    def total_wheels(cls):
        print(f'Total wheels: {cls.TOTAL_WHEEL}')


car_1 = Car()
car_2 = Car()
car_3 = Car()
Car.total_wheels()
car_1.total_wheels()

