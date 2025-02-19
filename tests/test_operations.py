# tests/test_operations.py
"""
Test cases for the main.py functionality.
This module tests the calculate function with various inputs and edge cases.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

def test_operation(a, b, operation, expected):
    """Test arithmetic operations."""
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
