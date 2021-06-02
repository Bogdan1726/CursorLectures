class Person:
    _name = 'Anna'
    age = 22

anna = Person()
print(anna._name)


setattr(anna, 'name', 'John')
print(anna._name)
print(getattr(anna, "name"))

setattr(anna, 'age', 21)
# print(anna.age)
print(getattr(anna, 'age'))

john = Person()
