def foo(x, y):
    return x * y


foo_1 = lambda x, y: x * y

print(foo(5, 10))
print(foo_1(5, 10))

foo_2 = lambda: True
print(foo_2())

foo_3 = lambda x: True if x % 2 == 0 else False
print(foo_3(2))
print(foo_3(3))
