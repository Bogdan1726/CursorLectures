from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError

    @abstractmethod
    def print_name(self):
        raise NotImplementedError


class Vegetables(Animals):

    def say_hello(self):
        pass

    def print_name(self):
        pass


class Fruits(Animals):

    def say_hello(self):
        pass




