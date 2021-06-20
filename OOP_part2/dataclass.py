from dataclasses import dataclass


@dataclass
class UserID:
    user_id: int
    default_user_id: int = 1


user = UserID(5)
print(user.user_id)
print(user.default_user_id)


@dataclass
class Article:
    """
    This class for holding the article content information
    """
    topic: int
    author: str
    language: str
    likes: int
    rate: float


python = Article(4, 'John', 'EN', 2345, 4.05)
python.reviewers = 'Anna'
python.rate = 34
print(python.reviewers)
print(type(python.topic))
print(python)
print(python.rate)



