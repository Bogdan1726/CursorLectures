# 1.
print('__________1__________')


class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, model='Lenovo'):
        self.model = model
        battery = Battery()
        screen = Screen()
        self.battery = battery
        self.screen = screen

    def __str__(self):
        return f'Model laptop: {self.model}\n' \
               f'Battery: {self.battery}\n' \
               f'Screen: {self.screen}'


class Battery:
    """
    Make the class with composition.
    """
    def __str__(self):
        return f'Latitude 7280  7.6V 60Wh'


class Screen:
    """
    Make the class with composition.
    """
    def __init__(self, diagonal=14):
        self.diagonal = diagonal

    def __str__(self):
        return f'Diagonal screen size {self.diagonal} inches'


laptop = Laptop()
print(laptop)


# 2.
print('__________2__________')


class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, brand, quantity_string, brand_string):
        self.brand = brand
        self.quantity_string = quantity_string
        self.brand_string = brand_string

    def __str__(self):
        return f'Brand: {self.brand}\n' \
               f'Quantity string: {self.quantity_string}\n' \
               f'Guitar string brand: {self.brand_string}'


class QuantityString:
    """
    Make the class with aggregation
    """
    def __init__(self, quantity=7):
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity}'


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, brand_string='FUSION'):
        self.brand_string = brand_string

    def __str__(self):
        return f'{self.brand_string}'


quantity = QuantityString()
string = GuitarString()
guitar = Guitar('Yamaha', quantity, string)
print(guitar)

# 3
print('__________3__________')


class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(a, b, c):
        result = a + b + c
        return f'Result: {a} + {b} + {c} = {result}'


print(Calc.add_nums(5, 6, 8))
calc = Calc()
print(calc.add_nums(4, 8, 12))
# 4*.
print('__________4__________')


class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])

    def __str__(self):
        return f'{self.list_of_ingredients}'


pasta_1 = Pasta(["tomato", "cucumber"])
print(f'will equal to: {pasta_1}')
pasta_2 = Pasta.bolognaise()
print(f'will equal to: {pasta_2}')
pasta_3 = Pasta.carbonara()
print(f'will equal to: {pasta_3}')

# 5*.
print('__________5__________')


class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert1 = Concert()
concert2 = Concert()

Concert.max_visitors_num = 50

print('concert1.max_visitors_num:', concert1.max_visitors_num)
concert1.visitors_count = 1000
print('concert1.visitors_count: ', concert1.visitors_count)

Concert.max_visitors_num = 5000

print('concert2.max_visitors_num:', concert2.max_visitors_num)
concert2.visitors_count = 2000
print('concert2.visitors_count: ', concert2.visitors_count)


# 6.
print('__________6__________')

import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


user_1 = AddressBookDataClass(1, 'Ivan', '0800-400-200-100', 'city.Lviv', 'ivan@gmail.com', '01.01.2000', 21)
print(f'Key: {user_1.key}\n'
      f'Name: {user_1.name}\n'
      f'Phone number: {user_1.phone_number}\n'
      f'City: {user_1.address}\n'
      f'Email: {user_1.email}\n'
      f'Birthday: {user_1.birthday}\n'
      f'Age: {user_1.age}')


# 7. Create the same class (6) but using NamedTuple
print('__________7__________')

import collections

AddressBookDataClassTwo = collections.namedtuple('AddressBookDataClassTwo',
                                ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

user_2 = AddressBookDataClassTwo(2, 'Gon', '777-777-777', 'New-York', 'gon@york.us', '02.02.1991', 30)

print(f'Key: {user_2.key}\n'
      f'Name: {user_2.name}\n'
      f'Phone number: {user_2.phone_number}\n'
      f'City: {user_2.address}\n'
      f'Email: {user_2.email}\n'
      f'Birthday: {user_2.birthday}\n'
      f'Age: {user_2.age}')
# 8.
print('__________8__________')


class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key: int, name: str, phone_number: str, address: str, email: str, birthday: str, age: int):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'{__class__.__name__}(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address = AddressBook(1, 'Bohdan', '0939804334', 'city.Dnipro', 'bogdan24ro@gmail.com', '1993', 27)
print(address)

# 9.
print('__________9__________')


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


user = Person()
user.age = 20
print(user.age)
print(Person.age)

# 10.
print('__________10__________')


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, 'Bogdan')
student.email = 'bogdan@gmail.com'
print(student.email)
student_email = getattr(student, 'email')
print(student_email)
setattr(student, 'name', 'Ivan')
print(student.name)
print(Student.name)

# 11*.
print('__________11__________')


class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        fahrenheit = (self._temperature * 1.8) + 32
        return f'Celsius {self._temperature} = Fahrenheit: {fahrenheit}'


celsius = Celsius(23)
print(celsius.fahrenheit)


