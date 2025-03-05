import pytest
from commands.divide_command import DivideCommand
from commands.multiply_command import MultiplyCommand
from commands.subtract_command import SubtractCommand
from commands.base_command import BaseCommand
from io import StringIO
from unittest.mock import patch

# Test for BaseCommand
def test_base_command_instantiation():
    """Ensure BaseCommand cannot be instantiated directly."""
    with pytest.raises(TypeError):
        _ = BaseCommand()  # This should raise a TypeError

# Tests for DivideCommand
def test_divide_command_name():
    """Test the name method of DivideCommand."""
    cmd = DivideCommand()
    assert cmd.name() == "divide"

@pytest.mark.parametrize("args, expected", [
    (["10", "0"], "Error while performing division: Cannot divide by zero"),
    (["10"], "Error: 'divide' requires exactly two numbers. Example: divide 10 2"),
    (["abc", "3"], "Invalid input. Please provide valid numbers. Received: ['abc', '3']"),
    ([], "Error: 'divide' requires exactly two numbers. Example: divide 10 2"),
    (["10", "3"], "Result of divide 10 and 3 is equal to 3.3333333333"),
])
def test_divide_command_edge_cases(capsys, args, expected):
    cmd = DivideCommand()
    cmd.execute(*args)
    output = capsys.readouterr().out.strip()
    if "Result of divide" in output:
        actual_number = float(output.split()[-1])
        expected_number = float(expected.split()[-1])
        assert actual_number == pytest.approx(expected_number, rel=1e-9)
    else:
        assert output == expected

# Tests for MultiplyCommand
def test_multiply_command_name():
    """Test the name method of MultiplyCommand."""
    cmd = MultiplyCommand()
    assert cmd.name() == "multiply"

@pytest.mark.parametrize("args, expected", [
    (["5", "text"], "Invalid input. Please provide valid numbers. Received: ['5', 'text']"),
    ([], "Error: 'multiply' requires exactly two numbers. Example: multiply 2 3"),
    (["3"], "Error: 'multiply' requires exactly two numbers. Example: multiply 2 3"),
    (["4", "5"], "Result of multiply 4 and 5 is equal to 20"),
])
def test_multiply_command_edge_cases(capsys, args, expected):
    cmd = MultiplyCommand()
    cmd.execute(*args)
    output = capsys.readouterr().out.strip()
    assert output == expected

# Tests for SubtractCommand
def test_subtract_command_name():
    """Test the name method of SubtractCommand."""
    cmd = SubtractCommand()
    assert cmd.name() == "subtract"

@pytest.mark.parametrize("args, expected", [
    (["7", "test"], "Invalid input. Please provide valid numbers. Received: ['7', 'test']"),
    ([], "Error: 'subtract' requires exactly two numbers. Example: subtract 5 3"),
    (["10"], "Error: 'subtract' requires exactly two numbers. Example: subtract 5 3"),
    (["10", "3"], "Result of subtract 10 and 3 is equal to 7"),
])
def test_subtract_command_edge_cases(capsys, args, expected):
    cmd = SubtractCommand()
    cmd.execute(*args)
    output = capsys.readouterr().out.strip()
    assert output == expected
