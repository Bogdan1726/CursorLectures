old_list = [1, 5, 4, 6, 8, 11, 3, 12]


def foo(x):
    if x % 2 == 0:
        return x
    else:
        return x + 1


new_list = list(map(foo, old_list))
print(new_list)

new_list = list(map(lambda x: x if x % 2 == 0 else x + 1, old_list))
print(new_list)
