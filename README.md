# Readme


# Dataclasses
[Python Docs](https://docs.python.org/3/library/dataclasses.html)

Dataclasses are a type of class meant for simplifying classes which are primarily used for storing data.

```Python
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    price: float
    quantity: float

    def price_per_amount (self) -> float:
        return self.price / self.quantity
```

Dataclasses come with automatically generated `__init__()`, `__repr__()`, and `__eq__()` methods. The type hints for each data member are required.

This largely helps reduce boilerplate code.

