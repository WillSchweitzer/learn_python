'''Storage Classes'''

from typing import TypeVar, Generic

from src.util import EmptyQueue

T = TypeVar('T')
type Path = str

class Queue (Generic[T]):
    """Queue class with specified datatype"""
    def __init__(self):
        self._storage: list[T] = []

    def enqueue (self, item: T) -> None:
        """Add an object to the end of the queue"""
        self._storage.append(item)

    def dequeue (self) -> T:
        """Remove and return an item from the front of the line"""
        if self.is_empty():
            raise EmptyQueue ("Attempting to dequeue from an empty container")
        return self._storage.pop(0)

    def is_empty (self) -> bool:
        """Returns true if the container is empty, false otherwise."""
        return not self._storage



class HashTable (dict[int, T]):
    '''Class to represent a list of students'''

    def __init__ (self, file: Path):
        """Initialize from filepath"""
        self._file: Path = file

    def __getitem__(self, key: str | int) -> T:
        return super().__getitem__(hash(key))

    def add (self, key: int | str, value: T) -> None:
        """Add an agent to the container"""
        self[hash(key)] = value

    def retrieve (self, key: str | int) -> T:
        """Retrieve the stored object with the matching key/id"""
        return self[hash(key)]
