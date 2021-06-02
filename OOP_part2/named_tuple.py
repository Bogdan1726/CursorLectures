"""
Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж, с тем дополнением,
что каждому элементу присваивается имя, по которому можно в дальнейшем получать доступ:
"""
import collections

Article = collections.namedtuple('Article', ['topic', 'author', 'language', 'likes', 'rate'])

python = Article('Python', 'John', 'EN', 2345, 4.25)

print(python[3])

print(python.rate)

print(python.topic)


