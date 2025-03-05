import pytest
from decimal import Decimal
from calculator import Calculator

def test_addition():
    """Test that the addition function works."""
    assert Calculator.add(Decimal('2'), Decimal('2')) == Decimal('4')

def test_subtraction():
    """Test that the subtraction function works."""
    assert Calculator.subtract(Decimal('2'), Decimal('2')) == Decimal('0')

def test_division():
    """Test that the division function works."""
    assert Calculator.divide(Decimal('2'), Decimal('2')) == Decimal('1')

def test_multiplication():
    """Test that the multiplication function works."""
    assert Calculator.multiply(Decimal('2'), Decimal('2')) == Decimal('4')

def test_divide_by_zero():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('10'), Decimal('0'))

def test_invalid_inputs():
    """Test that invalid inputs raise TypeError."""
    with pytest.raises(TypeError, match="Operands must be numeric values."):
        Calculator.add("five", 3)
    with pytest.raises(TypeError, match="Operands must be numeric values."):
        Calculator.subtract(10, None)
    with pytest.raises(TypeError, match="Operands must be numeric values."):
        Calculator.multiply({}, [])

def test_logging_error(caplog):
    """Test that logging captures calculation errors."""
    with caplog.at_level("ERROR"):
        with pytest.raises(TypeError):
            Calculator.add("text", 5)
    assert "Calculation error" in caplog.text
