'''Simple student class'''

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

    @property
    def odin (self) -> str:
        """Get the ODIN id."""
        return self.email.split('@', maxsplit=1)[0]


@dataclass
class Tutor (Student):
    """Tutor class, extension of student class"""

    def __str__ (self) -> str:
        return f"[TUTOR] {self.first} {self.last} ({self.age}) {self.email}: {self.gpa}"
