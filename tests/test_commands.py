"""This module contains tests for the command classes."""
from decimal import Decimal
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command():
    """Test the AddCommand class."""
    command = AddCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('5')

def test_subtract_command():
    """Test the SubtractCommand class."""
    command = SubtractCommand()
    assert command.execute(Decimal('5'), Decimal('3')) == Decimal('2')

def test_multiply_command():
    """Test the MultiplyCommand class."""
    command = MultiplyCommand()
    assert command.execute(Decimal('2'), Decimal('3')) == Decimal('6')

def test_multiply_by_zero():
    """Test multiplying a number by zero."""
    command = MultiplyCommand()
    assert command.execute(Decimal('5'), Decimal('0')) == Decimal('0')

def test_multiply_negative_numbers():
    """Test multiplying a negative number by a positive number."""
    command = MultiplyCommand()
    assert command.execute(Decimal('-2'), Decimal('3')) == Decimal('-6')

def test_divide_command():
    """Test the DivideCommand class."""
    command = DivideCommand()
    assert command.execute(Decimal('6'), Decimal('2')) == Decimal('3')

def test_divide_negative_numbers():
    """Test dividing a negative number by a positive number."""
    command = DivideCommand()
    assert command.execute(Decimal('-6'), Decimal('2')) == Decimal('-3')

def test_divide_by_zero():
    """Test division by zero (error case)."""
    command = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute(Decimal('10'), Decimal('0'))
        