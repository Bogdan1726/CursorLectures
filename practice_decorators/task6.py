# Напишіть декоратор який буде перейменовувавти вихідний файл функції яка створює цей файл.
#     @rename('test1.txt')
#     def create_file():
#         file_name = "copy.txt"
#         file = open(file_name, "w")
#         file.write("Your text goes here")
#         file.close()
#         return file_name
import os
import datetime
import uuid
​
​
def rename(filename):
    f = filename
    def decorator_rename(func):
        def inner(name):
            if os.path.exists(f):
                os.rename(func(name), str(uuid.uuid4()) + f)
            else:
                os.rename(func(name), f)
        return inner
    return decorator_rename
​
​
@rename('test1.txt')
def create_file(name):
    file = open(name, "w")
    file.write("Your text goes here")
    file.close()
    return name
​
​
create_file('new_file.txt')