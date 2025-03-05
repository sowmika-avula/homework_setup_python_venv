from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide
from commands.base_command import BaseCommand

fake = Faker()

class DummyCommand(BaseCommand):
    def name(self):
        return "dummy"

    def execute(self, *args):
        print("Dummy executed with args:", args)

def generate_test_data(num_records):
    """Generate test data for calculations."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Handle division by zero
        if operation_name == 'divide':  # Compare operation name instead of function
            b = Decimal('1') if b == Decimal('0') else b

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected
