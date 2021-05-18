# 1
d = {}
for num in range(1, 11):
    d[num] = num ** 2

print(d)

d = {num: num ** 2 for num in range(1, 11)}
print(d)

# 2
values = ['Ivanov', 'Petrov', 'Ivanov', 'Petrov']
key = ['ivanov@gmail.com', 'petr@gmail.com', 'ivan@mail.ru', 'petrov666@gmail.com']

dic = {}

for i in range(len(values)):
    dic[key[i]] = values[i]
print(dic)


dic = {key[x]: values[x] for x in range(len(values))}
print(dic)

# 3
s = ['Bogdan', 'Ivanov', 'Ivan', 'Ivanov', 'Ruslan', 'Ivanov']

q = {}
for i in range(len(s)):
    if i % 2 == 0:
        q[s[i]] = s[i+1]

print(q)

q = {s[i]: s[i+1] for i in range(len(s)) if i % 2 == 0}
print(q)

