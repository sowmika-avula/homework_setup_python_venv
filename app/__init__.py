# app/commands/command.py
from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    """Abstract base class for all command classes."""
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Execute the command with the given operands."""
        