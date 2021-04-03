from functools import reduce

numbers = [0, 1, 2, 3, 4]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


reduce(my_add, numbers)

summa = reduce(lambda a, b: a + b, numbers)
print(summa)

str_lst = ['I am student', 'Doing some work', 'Great student']
st_count = 0
for st_str in str_lst:
    st_count += st_str.count('student')
print(st_count)

st_count = reduce(lambda a, x: a + x.count('student'), str_lst, 0)
print(st_count)
