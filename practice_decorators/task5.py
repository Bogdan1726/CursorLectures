'''
Напишіть декоратор logger який буде зберігати логи у файлі, шлях до файлу можна
вказувати як
аргумент до декоратора.
​
@logger()
def myfunc1():
    pass
​
myfunc1()
​
Output: myfunc1 finished
File out.log created and contain the output
​
@logger(logfile='func2.log')
def myfunc2():
    pass
​
myfunc2()
​
Output: myfunc1 finished
File func2.log created and contain the output
'''
import random
​
​
def logger(logfile='default.log'):
    def logging_func(func):
        def inner(*args, **kwargs):
            with open(logfile, 'a') as file:
                file.write(f"{func.__name__} was called with ({args}, {kwargs}). Result is {func(*args, **kwargs)}\n")
            return func(*args, **kwargs)
​
        return inner
​
    return logging_func
​
​
@logger(logfile='func1.log')
def func1(a, b):
    return a + b
​
​
@logger(logfile='func2.log')
def func2(a, b):
    return a - b
​
​
@logger()
def func3(a, b):
    return a * b
​
​
# func1(random.randint(1, 100), random.randint(1, 100))
# func2(random.randint(1, 100), random.randint(1, 100))
func3(random.randint(1, 100), random.randint(1, 100))