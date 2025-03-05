from decimal import Decimal
from typing import Callable
import logging

# Avoid circular import issues by using local imports inside methods
from .operations import add, subtract, multiply, divide

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

class Calculator:
    """Provides a simple interface for performing calculations."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        try:
            from .calculation import Calculation  # Lazy import to avoid circular dependency
            from .calculations import Calculations  # Lazy import to avoid circular dependency

            # Validate inputs
            if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
                raise TypeError("Operands must be numeric values.")

            # Check division by zero
            if operation == divide and b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")

            # Perform calculation
            calculation = Calculation.create(a, b, operation)
            Calculations.add_calculation(calculation)
            return calculation.perform()

        except (TypeError, ZeroDivisionError) as e:
            logging.error(f"Calculation error: {e}")
            raise

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division."""
        return Calculator._perform_operation(a, b, divide)
    