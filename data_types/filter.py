# converts s to list
s = '13325'
print(list(s))


# filter to list
old_list = [1, 5, 4, 6, 8, 11, 3, 12]

# 1 function and list filter

# filter(function, iterable)


def filter_lis(lis):
    if lis % 2 == 0:
        return True
    return False


new_list_1 = f'Result: {list(filter(filter_lis, old_list))}'
print(new_list_1)

# 2 lambda function and list filter


new_list_2 = f'Result: {list(filter(lambda x: True if x % 2 == 0 else False, old_list))}'
print(new_list_2)

# filter to list
old_list_1 = ['Sammy', 'ashley', 'Jo', 'ally', 'Jackie', 'Charlie']

# 1 if len len element > 4
new_list_3 = f'Result: {list(filter(lambda x: True if len(x) > 4 else False, old_list_1))}'
print(new_list_3)

# 2 if element[0] is upper
new_list_4 = f'Result: {list(filter(lambda x: True if x[0].isupper() else False, old_list_1))}'
print(new_list_4)

old_list_2 = ['Sammy', '2', 'ashley', '5', 'Jo', 'ally', 'Jackie', '7', 'Charlie']

new_list_5 = f'Result{list(filter(lambda x: True if x.isdigit() else False, old_list_2))}'
print(new_list_5)
