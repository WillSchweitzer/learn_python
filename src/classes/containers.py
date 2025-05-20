'''Storage Classes'''

from typing import TypeVar, Generic

from src.util import EmptyQueue

T = TypeVar('T')

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
