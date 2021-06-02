"""
Композиция - это концепция, моделирующая отношения. Это позволяет создавать сложные типы, комбинируя
объекты других типов. Это означает, что класс Composite может содержать объект другого класса Component.
Это отношение означает, что у Composite есть компонент.
"""


class Book:

    def __init__(self):
        page_1 = Page('This is content of page 1')
        page_2 = Page('This is content of page 2')
        self.pages = [page_1, page_2]

    def __str__(self):
        return f'{self.pages}'


class Page:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'{self.content}'


book = Book()
print(book)
