# main.py
import sys
from decimal import Decimal, InvalidOperation
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
import importlib
import os

# Command registry
commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand()
}

def load_plugins():
    """Dynamically load commands from the plugins folder."""
    plugins_dir = "plugins"
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugins_dir}.{module_name}")
            for attr in dir(module):
                if attr.endswith("Command"):
                    command_class = getattr(module, attr)
                    commands[module_name] = command_class()

def calculate_and_print(a: str, b: str, operation_name: str):
    """Perform a calculation and print the result."""
    try:
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        operation = commands.get(operation_name)
        if operation:
            result = operation.execute(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def repl():
    """Read-Evaluate-Print-Loop for the calculator."""
    print("Welcome to the Calculator REPL. Type 'menu' for available commands.")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "exit":
            break
        elif user_input == "menu":
            print("Available commands:")
            for cmd in commands:
                print(f"- {cmd}")
        elif user_input in commands:
            try:
                a = Decimal(input("Enter first number: "))
                b = Decimal(input("Enter second number: "))
                result = commands[user_input].execute(a, b)
                print(f"Result: {result}")
            except InvalidOperation:
                print("Invalid input. Please enter valid numbers.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Type 'menu' for available commands.")

def main():
    """Entry point for the program."""
    load_plugins()
    repl()

if __name__ == '__main__':
    main()
    