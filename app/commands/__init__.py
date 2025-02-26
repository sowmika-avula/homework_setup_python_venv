# app/commands/__init__.py
"""This module defines the command interface and registers all available commands."""
from .command import Command
from .add import AddCommand
from .subtract import SubtractCommand
from .multiply import MultiplyCommand
from .divide import DivideCommand

__all__ = ['AddCommand', 'SubtractCommand', 'MultiplyCommand', 'DivideCommand']
