# Single responsibility principle
# Принцип единственной обязанности


# Bad practice
class DataTime:
    import datetime

    def __init__(self, name_city):
        self.name_city = name_city

    def print_date(self):
        return f'Date of the {self.name_city}: {self.datetime.datetime.now()}'

    def print_weather(self):
        temp = 32
        return f'Weather of the {self.name_city}: {temp}\u2103'

    def __str__(self):
        return f'{self.print_date()}\n' \
               f'{self.print_weather()}'


city = DataTime('Kiev')
print(city)


# Best practice

class DataTime:
    import datetime

    def __init__(self, name_city):
        self.name_city = name_city

    def print_date(self):
        return f'Date of the {self.name_city}: {self.datetime.datetime.now()}'

    def __str__(self):
        return f'{self.print_date()}'


date = DataTime('London')
print(date)


class Weather:

    def __init__(self, name_city):
        self.name_city = name_city

    def print_weather(self):
        temp = 32
        return f'Weather of the {self.name_city}: {temp}\u2103'

    def __str__(self):
        return f'{self.print_weather()}'


weather = Weather('Dubai')
print(weather)


# Open/closed principle
# Принцип открытости/закрытости

# Bad practice

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favorite':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
        if self.customer == 'my_wife':
            return self.price * 0


# Best practice

class Discount1:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favorite':
            return self.price * 0.2


class VIPDiscount(Discount1):
    def give_discount(self):
        return super().give_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    def give_discount(self):
        return super().give_discount() * 2


discount = Discount1('favorite', 3000)
print(discount.give_discount())
discount1 = VIPDiscount('favorite', 3000)
print(discount1.give_discount())
discount2 = SuperVIPDiscount('favorite', 3000)
print(discount2.give_discount())


# Liskov substitution principle
# Принцип подстановки Лисков


class Board:
    def __init__(self, board_type):
        self.board_type = board_type

    def get_board_type(self):
        return self.board_type


class UserLiskov:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def move(self, piece, position):
        piece.move(position)


class OldBoard(Board):

    def get_board_type(self):
        return self.board_type


board = Board('classic')
board_1 = OldBoard('Old classic')

user_white = UserLiskov('white', board)
user_black = UserLiskov('black', board_1)

# Interface segregation principle
# Принцип разделения интерфейса

from abc import ABC, abstractmethod


class Shape(ABC):
    # Best practice
    @abstractmethod
    def draw(self):
        raise NotImplementedError

    # Bad practice
    # def print(self):
    #     raise NotImplementedError


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        pass


# Dependency inversion principle
# Принцып инверсии зависимостей


class AuthForUser:
    def __init__(self, connect):
        self.connect = connect

    def auth(self, credentials):
        pass

    def is_auth(self):
        pass

    def last_login(self):
        pass


class AnonAuth(AuthForUser):
    pass


class GitHubAuth(AuthForUser):
    def last_login(self):
        pass


class Permission(AuthForUser):

    def has_persmission(self):
        pass


class IsLoggedInPermission(Permission):
    def last_login(self):
        pass
