class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def show_name(self):
        print(f'My name is {self.first_name}')


    def show_age(self):
        print(f'I am {self.age} years old')


class Student:
    def __init__(self, student_id, school_id):
        self.student_id = student_id
        self.school_id = school_id

    def get_student_id(self):
        print(f'Student ID: {self.student_id}')

    def get_school_id(self):
        print(f'School ID: {self.school_id}')


class Resident(Person, Student):
    def __init__(self, name, age, student_id, school_id):
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, school_id)


resident = Resident('Mike', 17, 12345678, 357)
print(resident.show_name())
print(resident.show_age())
print(resident.get_student_id())
print(resident.get_school_id())
