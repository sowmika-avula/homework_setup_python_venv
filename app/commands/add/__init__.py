"""This module defines the AddCommand class for performing addition."""
from decimal import Decimal
from app.commands import Command

class AddCommand(Command):
    """Command class for performing addition."""
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Add two numbers and return the result."""
        return a + b
    