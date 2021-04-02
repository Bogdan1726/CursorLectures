class Car:
    car_type = 'Regular car'

    def __init__(self, color, brand, model, engine_type):
        self.color = color
        self.brand = brand
        self.model = model
        self.engine_type = engine_type


car_1 = Car('Greeg', 'Ford', 'Mustang', 'Gasoline')
car_2 = Car('Red', 'Toyota', 'Prius', 'Electricity')
car_3 = Car('Blud', 'VW', 'Golf', 'Diesel')

print(f'Car 1 is a {car_1.car_type}')
print(f'Car 2 is a {car_2.__class__.car_type}')
print(f'Car 3 is a {car_3.car_type}')

print(f'{car_1.brand} is {car_1.color}')
print(f'{car_2.brand} is {car_2.model}')