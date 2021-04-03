rand_list = [5, 7, 1, 3]
print(sorted(rand_list))

print(sorted(rand_list, reverse=True))


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Alex = Employee('Alex', 20)
Anna = Employee('Anna', 18)
David = Employee('David', 30)
lst = [Anna, Alex, David]

lst.sort(key=lambda x: x.age)
print([item.name for item in lst])

str_lst = ['b', 'a', 'd']

print(sorted(str_lst))
