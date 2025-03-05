from decimal import Decimal
from typing import List, Optional

class Calculations:
    """Manages a history of Calculation instances."""

    history: List = []  # Remove Calculation type hint to prevent circular dependency

    @classmethod
    def add_calculation(cls, calculation):
        """Add a new calculation to the history."""
        from calculator.calculation import Calculation  # Import inside method to break circular import
        if isinstance(calculation, Calculation):  # Ensure it's a valid Calculation object
            cls.history.append(calculation)
        else:
            raise TypeError("Only Calculation instances can be added to history.")

    @classmethod
    def get_history(cls) -> List:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls):
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if hasattr(calc, 'operation') and calc.operation.__name__ == operation_name]
    