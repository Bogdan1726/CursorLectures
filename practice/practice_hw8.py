from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice, randint
from uuid import uuid4
from math import ceil


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self):
        raise NotImplementedError


class Predator(Animal):

    def eat(self):
        print(f'{__class__.__name__} питается')
        if self.current_power < self.max_power:
            self.current_power += (self.current_power // 2)
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        print(f'{__class__.__name__} {self.id} - Востановил здоровья на - {self.current_power // 2}(point) '
              f' Тукущее здоровья - {self.current_power}(power)')

    def __repr__(self):
        return f'Predator - {self.id}: ' \
               f'power={self.current_power} ' \
               f'speed={self.speed} '


class Herbivorous(Animal):

    def eat(self):
        print(f'{__class__.__name__} питается')
        if self.current_power < self.max_power:
            self.current_power += (self.current_power // 2)
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        print(f'{__class__.__name__} {self.id} - Востановил здоровья на - {self.current_power // 2}(point) '
              f' Тукущее здоровья - {self.current_power}(power)')

    def __repr__(self):
        return f'Herbivorous - {self.id}: ' \
               f'power={self.current_power} ' \
               f'speed={self.speed} '


AnyAnimal = []


class Forest:

    def __init__(self):
        self.animals = AnyAnimal

    def add_animal(self, animal: AnyAnimal):
        print(f'Новый {animal} добавлен в лес')
        self.animals.append(animal)

    def remove_animal(self, animal: AnyAnimal):
        print(f'{animal} - погиб')
        a = self.animals.index(animal)
        self.animals.pop(a)

    def any_predator_left(self):
        return all(isinstance(animal, Herbivorous) for animal in self.animals)

    def iter(self):

        animal_1 = choice(self.animals)
        if animal_1.current_power < 1:
            self.remove_animal(animal_1)

        animal_2 = choice(self.animals)
        if animal_2.current_power < 1:
            self.remove_animal(animal_2)

        if animal_1.__class__.__name__ == 'Herbivorous':
            animal_1.eat()
        else:
            if animal_2.__class__.__name__ == 'Predator':
                print('Вы не можете атаковать хищника')
            else:
                if animal_1.speed > animal_2.speed and animal_1.current_power > animal_2.current_power:
                    animal_1.eat()
                    animal_2.current_power -= (animal_1.current_power * 0.5)
                    print(f'{animal_2.__class__.__name__}: Потерял {animal_1.current_power * 0.5} power')
                else:
                    animal_1.current_power //= (animal_1.max_power * 0.3)
                    animal_2.current_power //= (animal_2.max_power * 0.3)
                    print(f'Добыча убежала, либо вам не хватило сил((')

    def __str__(self):
        return f'{self.animals}'


def animal_generator():
    generation = 1
    while True:
        print(f'Generation: {generation}')
        generation += 1
        generator_animal = choice((Herbivorous(randint(25, 100), randint(24, 100)),
                                   Predator(randint(25, 100), randint(24, 100))))
        generator_animal.id = uuid4()
        yield generator_animal


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(5):
        brute = next(nature)
        forest.add_animal(brute)
    while forest.any_predator_left() is False:
        forest.iter()
    print(AnyAnimal)
