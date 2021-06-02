"""
Агрегация - недельная форма композиции. Если вы удалите объект-контейнер,
объекты содержимого могут жить без объекта-контейнера.
"""


class Car:

    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission

    def __str__(self):
        return f'{self.engine} {self.transmission}'


class Engine:

    def __str__(self):
        return f'Engine - 2.0'


class Transmission:

    def __str__(self):
        return f'Transmission - АКПП'


engine_1 = Engine()
transmission_1 = Transmission()
car = Car(engine_1, transmission_1)
print(car)

