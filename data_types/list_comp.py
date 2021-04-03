lst = []
for num in range(10):
    lst.append(num ** 2)
print(lst)

lst_comp = [num ** 2 for num in range(10)]
print(lst_comp)

lst_comp_1 = [x for x in range(10) if x % 2 == 0]
print(lst_comp_1)

lst_comp_2 = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print(lst_comp_2)
