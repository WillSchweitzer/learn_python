'''Simple student class'''

from typing import Any
from dataclasses import dataclass

@dataclass
class Student:
    """Student class"""
    first: str
    last: str
    age: int
    gpa: float
    email: str

    def __str__ (self) -> str:
        return f"[STUDENT] {self.first} {self.last} ({self.age}) {self.email}: {self.gpa}"


    def __eq__ (self, other: Any) -> bool:
        return (
            (type(self) == type(other)) and
            (self.first == other.first) and
            (self.last == other.last) and
            (self.age == other.age) and
            (self.gpa == other.gpa) and
            (self.email == other.email)
        )

    @property
    def odin (self) -> str:
        """Get the ODIN id."""
        return self.email.split('@', maxsplit=1)[0]


@dataclass
class Tutor (Student):
    """Tutor class, extension of student class"""

    def __str__ (self) -> str:
        return f"[TUTOR] {self.first} {self.last} ({self.age}) {self.email}: {self.gpa}"

@dataclass
class Assistant (Student):
    """Assistant class, extension of student class"""

    def __str__ (self) -> str:
        return f"[TA] {self.first} {self.last} ({self.age}) {self.email}"
