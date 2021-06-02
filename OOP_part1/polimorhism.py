class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f'I am a cat. My name is {self.name}. '
              f'I am {self.age} years old.')

    def make_sound(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about_me(self):
        print(f'I am a dog. My name is {self.name} '
              f'I am {self.age} years old.')

    def make_sound(self):
        print('Bark')


cat = Cat('Kitty', 3)
dog = Dog('Demy', 1)

for animal in (cat, dog):
    animal.make_sound()
    animal.about_me()
