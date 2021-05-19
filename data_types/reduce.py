from functools import reduce

numbers = [1, 2, 3, 4, 5]


def my_add(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")
    return result


reduce(my_add, numbers)

# 2

summa = reduce(lambda a, b: a * b, numbers)
print(summa)

# 3
str_lst = ['1', '2', '2', '4', '4', '5', '5']


st_count = reduce(lambda a, x: a + x.count('4'), str_lst, 0)
print(f'Result: {st_count}')


# 4
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(f'Result: {cap_count}')


cap_count_1 = reduce(lambda a, x: a + x.count('капитан'), sentences, 0)
print(f'Result: {cap_count_1}')

