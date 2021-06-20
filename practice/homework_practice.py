import random
from abc import ABC, abstractmethod

VEGETABLES = ['Red tomato']
FRUITS = ['King']

states = {0: 'nothing', 1: 'flowering', 2: 'green', 3: 'red', 4: 'wormy'}


class GardenMetaClass(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def __repr__(self):
        return self.gardener

    def show_the_garden(self):
        print(f'The garden has such vegetables: {self.vegetables}')
        print(f'Also garden has such fruits: {self.fruits}')
        print(f'And such pests: {self.pests}')
        print(f'The maintainer of the garden is {self.gardener}')


class Vegetables(ABC):

    def __init__(self, vegetable_type, name):
        self.state = 0
        self.vegetable_type = vegetable_type
        self.name = name

    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
            print(f'{vegetable_type} in VEGETABLES')
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {vegetable_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Fruit(ABC):

    def __init__(self, fruits_type, name):
        self.state = 0
        self.fruits_type = fruits_type
        self.name = name

    @property
    def fruits_type(self):
        return self._fruits_type

    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
            print(f'{fruits_type} in VEGETABLES')
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {fruits_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Pests:

    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    @abstractmethod
    def eat(self):
        raise NotImplementedError('The method is missing.')


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('The method is missing.')


class Tomato(Vegetables):

    def __init__(self, vegetable_type, name, index):
        self.index = index
        self.state = 0
        super(Tomato, self).__init__(vegetable_type, name)

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Vegetable: {self.vegetable_type}-{self.index} states: {states.get(self.state)}')

    def __repr__(self):
        return f'{self.vegetable_type} {self.index} is {states.get(self.state)}'


class TomatoBush(Tomato):

    def __init__(self, vegetable_type, name, num):
        super(TomatoBush, self).__init__(vegetable_type, name, index=0)
        self.tomatoes = [Tomato(vegetable_type, name, index) for index in range(1, num+1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def provide_harvest(self):
        self.tomatoes = []


class Apple(Fruit):

    def __init__(self, fruits_type, name, index):
        self.index = index
        self.state = 0
        super(Apple, self).__init__(fruits_type, name)

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Fruits: {self.fruits_type}-{self.index} states: {states.get(self.state)}')

    def __repr__(self):
        return f'{self.fruits_type} {self.index} is {states.get(self.state)}'


class AppleTree(Apple):

    def __init__(self, fruits_type, name,  num):
        super(AppleTree, self).__init__(fruits_type, name, index=0)
        self.apples = [Apple(fruits_type, name, index) for index in range(1, num+1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def provide_harvest(self):
        self.apples = []


class BadPests(Pests):

    def __init__(self, pests_type, quantity, plants):
        self.plants = plants
        super(BadPests, self).__init__(pests_type, quantity)

    def eat(self):
        for pest in range(random.randint(1, self.quantity)):
            tomato_bush.tomatoes.pop(-1)
            if len(tomato_bush.tomatoes) == 0:
                break
        for pest in range(random.randint(1, self.quantity)):
            apple_tree.apples.pop(-1)
            if len(apple_tree.apples) == 0:
                break

    def __str__(self):
        return f'{self.pests_type} is {self.quantity}'


class StarGardener(Gardener):

    def __init__(self, name, plants):
        super(StarGardener, self).__init__(name, plants)
        self.name = name
        self.plants = plants

    def harvest(self):
        print(f'Gardener is harvesting')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.provide_harvest()
                print('Harvesting is finished.')
            else:
                print('Too early! Your plants is not ripe.')

    def poison_pests(self):
        pests.quantity //= 2

    def handling(self):
        print('Gardner is working...')
        for plant in self.plants:
            plant.grow_all()
        print('Gardner is finished')

    def check_states(self):
        plantation = [tomato_bush.tomatoes, apple_tree.apples]
        for plant in plantation:
            for el in plant:
                if el.is_ripe():
                    return True
            return False

    def __str__(self):
        return self.name


if __name__ == '__main__':
    apple_tree = AppleTree('King', 'Golden', 5)
    tomato_bush = TomatoBush('Red tomato', 'Cherry', 4)
    tom = StarGardener('Tom', [tomato_bush, apple_tree])
    for _ in range(3):
        tom.handling()
    pests = BadPests('worms', 6, [tomato_bush, apple_tree])
    tom.poison_pests()
    pests.eat()
    garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=tom)
    garden.show_the_garden()


