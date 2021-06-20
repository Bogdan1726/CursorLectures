
def is_adult(age):
    if age > 18:
        return True
    else:
        return False


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_valid_age(self):
        if is_adult(self.age) is False:
            return f'Sorry'
        return f'Good'

    @staticmethod
    def is_adult(x):
        if x > 18:
            return True
        else:
            return False


anna = Person('Anna', 15)
print(anna.is_valid_age())
print(is_adult(24))
