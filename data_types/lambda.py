# returns of the x
# 1 function
def return_x(x):
    return x


print(return_x(5))
# 2  lambda function

num_x = lambda x: x

print(num_x(3))

# returns x * y
# 1 function


def foo(x, y):
    return x * y


print(foo(5, 10))

# 2 lambda function


foo_1 = lambda x, y: x * y

print(foo_1(5, 10))

# returns True if it is even
# 1 function


def foo_3(x):
    if x % 2 == 0:
        return True
    return False


print(foo_3(4))
print(foo_3(3))

# 2 lambda function
foo_3 = lambda x: True if x % 2 == 0 else False
print(foo_3(2))
print(foo_3(3))


# returns factorial num x

# 1 function
def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial = factorial*i
    return f'Factorial {x}: {factorial}'


print(fact(5))

# 2 lambda function
fact = lambda x: 1 if x == 0 else x * fact(x-1)
a = 5
print(f'Factorial {a}: {fact(a)}')


# 5 * 24
# 4 * 6
# 3 * 2
# 2 * 1

# returns x else x < y else y
# 1 function
def foo(x, y):
    if x < y:
        return x
    else:
        return y


print(foo(5, 4))

# 2 lambda function
foo = lambda x, y: x if x < y else y
print(foo(6, 10))


def foo_5(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo_5(3, 6, 3))


foo_6 = lambda x, y, z: z if y < x and x > z else y
print(foo_6(3, 8, 8))


# returns summa
# 1 function
def summa(*args):
    return f'Result: {sum(args)}'


print(summa(3, 345, 23432, 454, 343))

# 2  lambda function
summa_1 = lambda *args: f'Result: {sum(args)}'
print(summa_1(3, 5365, 454, 34534))

a = 5