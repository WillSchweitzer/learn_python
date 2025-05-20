'''Simple student class'''

class Student:
    """Student class"""
    def __init__(self, data: dict[str, str | int | float]):
        self._first: str = str(data["first"])
        self._last: str = str(data["last"])
        self._age: int = int(data["age"])
        self._gpa: float = float(data["gpa"])
        self._email: str = str(data["email"])

    def __str__ (self) -> str:
        return f"[STUDENT] {self._first} {self._last} ({self._age}) {self._email}: {self._gpa}"

    @property
    def odin (self) -> str:
        """Get the ODIN id."""
        return self._email.split('@', maxsplit=1)[0]


class Tutor (Student):
    """Tutor class, extension of student class"""

    def __str__ (self) -> str:
        return f"[TUTOR] {self._first} {self._last} ({self._age}) {self._email}: {self._gpa}"
