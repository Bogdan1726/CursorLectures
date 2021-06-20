class Person:
    _name = 'Anna'
    age = 22


anna = Person()

print(getattr(anna, '_name'))

setattr(anna, '_name', 'John')
print(getattr(anna, '_name'))

setattr(anna, 'age', 21)
# print(anna.age)
print(getattr(anna, 'age'))

john = Person()
