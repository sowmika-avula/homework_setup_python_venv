# commands/base_command.py
from abc import ABC, abstractmethod
# commands/__init__.py

class BaseCommand(ABC):
    """Abstract base class for all commands in the commands branch."""

    @abstractmethod
    def name(self) -> str:
        """Return the command name as used in the REPL."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, *args) -> None:
        """Execute the command logic (with debugging in the commands branch)."""
        raise NotImplementedError