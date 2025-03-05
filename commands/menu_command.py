from commands.base_command import BaseCommand

class MenuCommand(BaseCommand):
    def name(self) -> str:
        return "menu"

    def execute(self, *args) -> None:
        """
        Usage:
          menu

        Lists all available commands.
        """
        from plugin_loader import load_plugins  # Delayed import to avoid circular dependencies

        commands = load_plugins("commands")
        print("Available commands:")

        for cmd_name in sorted(commands.keys()):
            print(f"  {cmd_name}")
            