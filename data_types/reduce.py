from functools import reduce

numbers = [0, 1, 2, 3, 4]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


reduce(my_add, numbers)

summa = reduce(lambda a, b: a + b, numbers)
print(summa)

str_lst = ['1', '2', '2', '4', '4', '5', '5']


st_count = reduce(lambda a, x: a + x.count('4'), str_lst, 0)
print(st_count)


