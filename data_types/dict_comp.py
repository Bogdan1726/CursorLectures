d = {}
for num in range(1, 11):
    d[num] = num ** 2

print(d)

d = {num: num ** 2 for num in range(1, 11)}
print(d)