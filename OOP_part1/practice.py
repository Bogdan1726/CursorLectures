# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    default_max_speed = 60
    default_mileage = 10000

    def __init__(self, max_speed=default_max_speed, mileage=default_mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_characteristics(self):
        return f'Maximum speed: {self.max_speed}-km\nDriven mileage - {self.mileage}-km'


print('__________1__________')
car = Vehicle(max_speed=80, mileage=12000)
print(car.print_characteristics())

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will
# have seating_capacity own method


class Bus(Vehicle):
    default_seating_capacity = 25

    def __init__(self, max_speed, mileage, seating_capacity=default_seating_capacity):
        self.seating_capacity = seating_capacity
        super(Bus, self).__init__(max_speed, mileage)

    def print_characteristics_bus(self):
        return f'Seating capacity: {self.seating_capacity}'


print('__________2__________')
bus = Bus(50, 13000)
print(bus.print_characteristics())
print(bus.print_characteristics_bus())


# 3. Determine which class a given Bus object belongs to (Check type of an object)
print('__________3__________')
print(type(bus))
print(issubclass(Bus, Vehicle))

# 4. Determine if School_bus is also an instance of the Vehicle class
print('__________4__________')
print(isinstance(bus, Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes
print('__________5__________')


class School:
    default_get_school_id = 1
    default_number_of_students = 10

    def __init__(self, get_school_id=default_get_school_id, number_of_students=default_number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def print_characteristics_school(self):
        return f'School id: {self.get_school_id}\nStudent number: {self.number_of_students}'


school = School(get_school_id=2)
print(school.print_characteristics_school())

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own -
# bus_school_color
print('__________6__________')


class SchoolBus(School, Bus):

    default_bus_school_color = 'yellow'

    def __init__(self, max_speed, mileage, seating_capacity, get_school_id, number_of_students,
                 bus_school_color=default_bus_school_color):
        self.bus_school_color = bus_school_color
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        School.__init__(self, get_school_id, number_of_students)

    def __str__(self):
        return f'School Bus color: {self.bus_school_color}'


school_bus = SchoolBus(70, 7000, 21, 5, 20)
print(school_bus.print_characteristics())
print(school_bus.print_characteristics_bus())
print(school_bus.print_characteristics_school())
print(school_bus)

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.
print('__________7__________')


class Bear:

    default_name = 'Grizzly'
    default_age = 10

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age

    def about_my(self):
        return f'I am Bear. My name is: {self.name}\n' \
               f'My am {self.age} old years\n'

    def make_sound(self):
        return f'Bear'


bear = Bear()


class Wolf:

    default_name = 'Grey wolf'
    default_age = '8'

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age

    def about_my(self):
        return f'I am Wolf. My name is: {self.name}\n' \
               f'My am {self.age} old years'

    def make_sound(self):
        return f'Wolf'


wolf = Wolf()


animals = (bear, wolf)
for animal in animals:
    print(animal.make_sound())
    print(animal.about_my())

# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
print('__________8__________')


class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        return f'Your city is too small'

    def __str__(self):
        return f'{self.population}'


city_1 = City('Kiev', 1300000)
print(city_1)
city_2 = City('Dnipro', 1000)
print(city_2)


# 9. Override a printable string representation of the City class and return: The population of the city {name} is
# {population}
print('__________9__________')


class City_2:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City_2, cls).__new__(cls)
        if population > 1500:
            return instance
        return f'Your city is too small'

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city = City_2('London', 20000)
print(city)

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater t
# han 10. And perform this add (+) of two instances.
print('__________10__________')


class Count:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 or other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'


num = Count(5)
num_1 = Count(10)
summa = num + num_1
print(summa)

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can
# be called like a function.
# Create a new class with __call__ method and define this call to return sum.
print('__________11__________')


class CallArea:

    def __call__(self, *args):
        return sum(args)


summa = CallArea()
print(f'Summa: {summa(3, 7, 33, 4234)}')
# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
print('__________12__________')


class MyOrder:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))

