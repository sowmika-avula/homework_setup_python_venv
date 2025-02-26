# app/commands/multiply/__init__.py
"""This module defines the MultiplyCommand class for performing multiplication."""
from decimal import Decimal
from app.commands import Command

class MultiplyCommand(Command):
    """Command class for performing multiplication."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Multiply two numbers and return the result."""
        return a * b
    
    