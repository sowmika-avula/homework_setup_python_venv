"""This module contains tests for the main application."""
from main import calculate_and_print

def test_calculate_and_print_add(capsys):
    """Test the calculate_and_print function with addition."""
    calculate_and_print("2", "3", "add")
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 2 add 3 is equal to 5"

def test_calculate_and_print_subtract(capsys):
    """Test the calculate_and_print function with subtraction."""
    calculate_and_print("5", "3", "subtract")
    captured = capsys.readouterr()
    assert captured.out.strip() == "The result of 5 subtract 3 is equal to 2"

def test_calculate_and_print_divide_by_zero(capsys):
    """Test the calculate_and_print function with division by zero."""
    calculate_and_print("10", "0", "divide")
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Cannot divide by zero"
    