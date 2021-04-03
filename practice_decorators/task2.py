'''
    Створіть декоратор (Timer), який засікає час роботу функції. Для створення декоратора використайте class, а не function.
​
    def init(self, func): self.function = func def call(self, *args, **kwargs):
​
@Timer
def some_function(delay):
    from time import sleep
​
    # Introducing some time delay to
    # simulate a time taking function.
    sleep(delay)
​
some_function(3)
'''
import time
​
​
class Timer:
    def __init__(self, function1, function2):
        self.function1 = function1
        self.function2 = function2
​
    def __call__(self, *args, **kwargs):
        start1 = time.time()
        self.function1(*args, **kwargs)
        time1 = time.time() - start1
        print(f'time remained for function1: {time1} sec')
        start2 = time.time()
        self.function2(*args, **kwargs)
        time2 = time.time() - start2
        print(f'time remained for function2: {time2} sec')
        print(f'total time remained for function1 and function2: {time1 + time2} sec')
​
​
def some_function1(delay):
    for i in range(0, delay):
        print(i)
        time.sleep(1)
​
​
def some_function2(delay):
    for i in range(1, delay):
        print(i)
        time.sleep(1)
​
​
timer = Timer(some_function1, some_function2)
timer(4)