students_list = ['Andrii', 'Anna', 'Rostyslav']
for student in students_list:
    str_1 = f"I am student and my name is {student}"
    print(str_1)

print("Anna has {} flowers and {} balloons".format(5, 3))

print("Anna has {1} flowers and {0} balloons".format(5, 3))

print("Anna has {flowers} flowers and {balloons} balloons".format(flowers=5, balloons=3))

verb = "flies"
preposition = "like"
print(f"Time {verb} {preposition} an arrow. Fruit {verb} {preposition} a banana.")

name = "boo"
friend_name = "foo"
print('Hey %s, there is you friend %s!' % (name, friend_name))


