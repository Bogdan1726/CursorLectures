# Напишіть програму, яка виводить частину послідовності 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ....
# На вхід приймається значення n - кількість елементів послідовності, які мають бути виведенні
#
# Наприклад, якщо n = 7, то програма має вивести 1 2 2 3 3 3 4. Sample Input: 7 Sample Output: 1 2 2 3 3 3 4
#
# Напишіть декоратор який виведе результат як str.
from functools import wraps
​
​
def str_from_list(func):
    @wraps(func)
    def inner(lst):
        return ''.join([str(x) + ' ' for x in func(lst)])
        # return ' '.join(map(lambda x: str(x), func(lst)))
    return inner
​
​
@str_from_list
def list_from(n):
    lst = [str(x) * x for x in range(1, n + 1)]
    return list(map(lambda x: int(x), ''.join(lst)[:n]))
​
​
print(list_from(7))