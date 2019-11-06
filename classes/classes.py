import typing


class Person:
    def __init__(self, age, firstName, lastName):
        self.age = age
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Options:
    def __init__(
        self, name, message,
    ):
        self.name = name
        self.message = message

    def run(self):
        return self.message

    def __str__(self):
        return self.name
