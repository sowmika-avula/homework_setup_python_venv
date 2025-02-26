"""This module defines the Calculation class for representing a single calculation."""
from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a single calculation with two operands and an operation."""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize a Calculation instance."""
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Create a new Calculation instance."""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Perform the calculation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
    