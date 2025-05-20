'''Storage Classes'''

from typing import TypeVar, Generic

from src.util import EmptyQueue

T = TypeVar('T')

class ClassQueue (Generic[T]):
    def __init__(self):
        self._storage: list[T] = []

    def enqueue (self, item: T) -> None:        
        self._storage.append(item)

    def dequeue (self) -> T:
        if self.is_empty():
            raise EmptyQueue ("Attempting to dequeue from an empty container")
        return self._storage.pop(0)
    
    def is_empty (self) -> bool:
        return not self._storage