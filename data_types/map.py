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


names = ['Harry', 'Suzy', 'Al', 'Mark']


def f(x):
    if x == 'Harry':
        return x + ': 27 years'
    return x + ': 0 years'


news_names = list(map(f, names))
print(news_names)


news_names_2 = list(map(lambda x: x + ': 27 years' if x == 'Harry' else x + ': 0 years', names))
print(news_names_2)


list_of_words = ['one', 'two', 'list', 'dict']

new_list_of_words = list(map(str.upper, list_of_words))
print(new_list_of_words)


squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))
print(squares)
