'''Simple student class'''

class Student:
    def __init__(self, first: str, last: str, age: int, gpa: float, email: str):
        self._first = first
        self._last = last
        self._age = age
        self._gpa = gpa
        self._email = email
        self._odin = email.split('@')[0]


class Tutor (Student):
    def __init__(self, first: str, last: str, age: int, gpa: float, email: str):
        super().__init__(first, last, age, gpa, email)