# recursion + factorial
# Напишіть функцію, яка рекурсивно рахує факторіал, а заодно декоратор,
# який перевіряє чи вхідне значення ціле та позитивне число:
# def argument_test_natural_number(f):
#     # check is arg to f is int and > 0, raise error otherwise
from functools import wraps
​
​
class NotIntNegativeError(BaseException):
    pass
​
​
def int_not_negative(func):
    @wraps(func)
    def inner(n_1):
        if n_1 > 0 and isinstance(n_1, int):
            return func(n_1)
        raise NotIntNegativeError
    return inner
​
​
def multiply_by_two(number_value):
    def number_decorator(func):
        @wraps(func)
        def inner(number):
            return func(number) * number_value
​
        return inner
    return number_decorator
​
​
@multiply_by_two(4)
@int_not_negative
def factorial(n):
    if n <= 1:
        return n
    return 5 * n
​
​
print(factorial(5))