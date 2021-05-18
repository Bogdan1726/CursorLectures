from functools import reduce

lis = ['Bob', '25', 'Joni', '33', 'Gvi' '27']


def f(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


print(reduce(f, lis))




