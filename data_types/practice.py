# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(f'__________1__________')
print(f'id int_a: {id(int_a)}\n'
      f'id str_b: {id(str_b)}\n'
      f'id set_c: {id(set_c)}\n'
      f'id lst_d: {id(lst_d)}\n'
      f'id dict_e: {id(dict_e)}')

# 2. Append 4 and 5 to the lst_d and define the id one more time.
print(f'__________2__________')
lst_d.extend([4, 5])
print(f'id int_a: {id(int_a)}\n'
      f'id str_b: {id(str_b)}\n'
      f'id set_c: {id(set_c)}\n'
      f'id lst_d: {id(lst_d)}\n'
      f'id dict_e: {id(dict_e)}')
# 3. Define the type of each object from step 1.
print(f'__________3__________')
print(f'type int_a: {type(int_a)}\n'
      f'type str_b: {type(str_b)}\n'
      f'type set_c: {type(set_c)}\n'
      f'type lst_d: {type(lst_d)}\n'
      f'type dict_e: {type(dict_e)}')
# 4*. Check the type of the objects by using isinstance.
print(f'__________4__________')
print(f'int_a: {isinstance(int_a, int)}\n'
      f'str_b: {isinstance(str_b, str)}\n'
      f'set_c: {isinstance(set_c, set)}\n'
      f'lst_d: {isinstance(lst_d, list)}\n'
      f'dict_e: {isinstance(dict_e, dict)}')
# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# 5. With .format and curly braces {}
print(f'__________5__________')
print('Anna has {} apples and {} peaches.'.format(5, 3))
# 6. By passing index numbers into the curly braces.
print(f'__________6__________')
print('Anna has {1} apples and {0} peaches.'.format(5, 3))
# 7. By using keyword arguments into the curly braces.
print(f'__________7__________')
print('Anna has {apple} apples and {peach} peaches.'.format(apple=7, peach=4))
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print(f'__________8__________')
print('Anna has {0:5} apples and {1:3} peaches.'.format(5, 3))
# 9. With f-strings and variables
print(f'__________9__________')
print(f'Anna has {6} apples and {2} peaches.')
# 10. With % operator
print(f'__________10__________')
print('Anna has % s apples and % s peaches.' % (2, 5))
# 11*. With variable substitutions by name (hint: by using dict)
print(f'__________11__________')
data_dict = {"a": 6, "b": 8}
print("Anna has %(a)s apples and %(b)s peaches." % data_dict)
# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)


# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
print(f'__________12__________')
print(f'Result lst: {lst}')
list_comprehension_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(f'Result list comprehension: {list_comprehension_1}')

# 13. Convert (2) to regular for with if-else
print(f'__________13__________')
lst_1 = []
for num in range(10):
    if num % 2 == 0:
        lst_1.append(num // 2)
    else:
        lst_1.append(num * 10)

print(f'Result list comprehension: {list_comprehension}')
print(f'Result lst: {lst_1}')

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2


# (4)
d_1 = {}
for num in range(1, 11):
    if num % 2 == 1:
        d_1[num] = num ** 2
    else:
        d_1[num] = num // 0.5


# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

# (6)
dict_comprehension_2 = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

# 14. Convert (3) to dict comprehension.
print(f'__________14__________')
print(f'Result dict: {d}')
dict_comprehension_4 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(f'Result dict comprehension: {dict_comprehension_4}')
# 15*. Convert (4) to dict comprehension.
print(f'__________15__________')
print(f'Result dict: {d_1}')
dict_comprehension_3 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(f'Result dict comprehension: {dict_comprehension_3}')
# 16. Convert (5) to regular for with if.
print(f'__________16__________')
print(f'Result dict_comprehension: {dict_comprehension}')
d_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_2[x] = x ** 3
print(f'Result dict: {d_2}')
# 17*. Convert (6) to regular for with if-else.
print(f'__________17__________')
print(f'Result dict_comprehension: {dict_comprehension_2}')
d_3 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        d_3[x] = x ** 3
    else:
        d_3[x] = x
print(f'Result dict: {d_3}')

# Lambda:


# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

# (8)
foo_1 = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
print(f'__________18__________')
foo_2 = lambda x, y: x if x < y else y
print(f'Result def: {foo(4, 6)}')
print(f'Result lambda: {foo_2(4, 6)}')
# 19*. Convert (8) to regular function
print(f'__________19__________')


def foo_3(x, y, z):
    if y < x and x > z:
        return z
    return y


print(f'Result lambda: {foo_1(3, 5, 8)}')
print(f'Result def: {foo_3(3, 5, 8)}')


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print(f'__________20__________')
print(f'Result sort from min to max: {sorted(lst_to_sort)}')
# 21. Sort lst_to_sort from max to min
print(f'__________21__________')
print(f'Result sort from max to min: {sorted(lst_to_sort, reverse=True)}')
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(f'__________22__________')
new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(f'Result: {new_lst_to_sort}')

# 23*. Raise each list number to the corresponding number on another list:
print(f'__________23__________')

list_A = [2, 3, 4]
list_B = [5, 6, 7]
new_lst = list(map(lambda x, y: x + y, list_A, list_B))
print(f'Result: {new_lst}')

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
print(f'__________24__________')
from functools import reduce
new_lst_1 = reduce(lambda x, y: x + y, lst_to_sort)
print(f'Result: {new_lst_1}')

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(f'__________25__________')
new_lst_2 = list(filter(lambda x: True if x % 2 == 1 else False, lst_to_sort))
print(f'Result: {new_lst_2}')

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(f'__________26__________')
b = [i for i in range(-10, 10)]
new_b = list(filter(lambda x: True if x < 0 else False, b))
print(f'Result: {new_b}')
# 27*. Using the filter function, find the values that are common to the two lists:
print(f'__________27__________')
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
new_lst_3 = list(filter(lambda x: True if x in list_2 else False, list_1))
print(f'Result: {new_lst_3}')

