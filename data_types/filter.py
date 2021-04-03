
old_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), old_list))

print(new_list)


def foo(x):
    if x % 2 == 0:
        return True
    return False


new_list_1 = list(filter(foo, old_list))

print(new_list_1)
