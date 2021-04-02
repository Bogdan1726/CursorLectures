class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_name(self):
        print(f'My name is {self.name} {self.surname}')


person = Person("Anna", 'Acco')
person.print_name()


class Student(Person):
    def __init__(self, name, surname, school_name):
        self.school_name = school_name
        self.name = name
        self.surname = surname
        super().__init__(name, surname)

    def school(self):
        print(f'My school name is: {self.school_name}')


student = Student('Mike', 'Torso', 'LNU')
student.print_name()
student.school()

print(isinstance(student, Person))

class Teacher(Person):
    pass

print(issubclass(Teacher, Person))
