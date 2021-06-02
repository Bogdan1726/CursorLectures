class Car:

    # Статические поля (переменные класса)
    car_type = 'Regular car'

    # method classes or attribute classes
    def __init__(self, color, brand, model, engine_type):
        # Динамические поля (переменные объекта)
        self.color = color
        self.brand = brand
        self.model = model
        self.engine_type = engine_type

    # method classes or attribute classes
    def __str__(self):
        return f'{self.brand} {self.model} {self.color} {self.engine_type}'


# objects classes
car_1 = Car('Green', 'Ford', 'Mustang', 'Gasoline')
car_2 = Car('Red', 'Toyota', 'Prius', 'Electricity')
car_3 = Car('Blue', 'VW', 'Golf', 'Diesel')
print(car_1)
print(car_2)
print(car_3)

print(f'Car 1 is a {car_1.car_type}')
print(car_1.color)
print(car_2.model)
print(f'{car_1.brand} is {car_1.color}')
print(f'{car_2.brand} is {car_2.model}')

print(dir(car_1))  # list of the attributes classes

