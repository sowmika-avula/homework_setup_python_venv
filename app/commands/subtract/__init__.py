"""This module defines the SubtractCommand class for performing subtraction."""
from decimal import Decimal
from app.commands import Command

class SubtractCommand(Command):
    """Command class for performing subtraction."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Subtract two numbers and return the result."""
        return a - b
    