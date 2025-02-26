"""This module defines the DivideCommand class for performing division."""
from decimal import Decimal
from app.commands import Command

class DivideCommand(Command):
    """Command class for performing division."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Divide two numbers and return the result."""
        if b == Decimal('0'):
            raise ValueError("Cannot divide by zero")
        return a / b
    