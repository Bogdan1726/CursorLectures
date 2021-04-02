a = 5
if a == 5:
    a += 1
print(a)

if True:
    print(1)

if a > 1:
    a += 1
print(a)

if a == 5:
    a = a * 5
else:
    a = 0
print(a)

a = 7


if a == 5:
    print('a')
elif a == 6:
    print('b')
elif a == 7:
    print('c')
else:
    print('None')

b = 0
while b < 8:
    b += 1
    print(b)

# a = 0
# while a == 0:
#     print("a")

a = 0
while a >= 0:
    if a == 7:
        break
    a += 1
    print(a)

c = -1
while c < 10:
    c += 1
    if c >= 7:
        continue
    print(c)

for i in range(5):
    a = i
    print(i)

lst = [1, 5, 8]
for i in lst:
    print(i ** 2)

def test(a):
    print(a.append(1))

test(lst)

print(lst)

def return_list():
    a = [1, 2]
    print(a)
    return a

def append_list(a):
    a.append(1)
    print(a)

append_list(return_list())
old_list = return_list()
