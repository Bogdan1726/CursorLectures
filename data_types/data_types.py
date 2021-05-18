a = None

b = True
b = False

c = 4
c = 4.5

l = [1, 2, 3]
t = (1, 2, 3)

s = "string"

s = {1, 2, 3}

d = {"key": "value"}


b = 6
c = "str"
print(id(b))
print(id(c))

print(type(b))
print(type(c))

print(isinstance(b, str))

import keyword
print(f"Python keywords: {keyword.kwlist}")
print(keyword.iskeyword('try'))

int_1 = 5
print(id(int_1))
int_1 += 1
print(id(int_1))

list_1 = [1, 2, 3]
print(id(list_1))
list_1.append(4)
print(id(list_1))

