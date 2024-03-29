import os
import logging
import importlib
from App.CalculatorContext import CalculatorContext
from App.HistoryManager import HistoryManager
from App.strategies.base_strategy import OperationStrategy
from .strategies.arithmetic_strategies import AddOperationStrategy, SubtractOperationStrategy, MultiplyOperationStrategy, DivideOperationStrategy

class CalculatorApp:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.history_manager = HistoryManager()
        self.strategies = {
            "add": AddOperationStrategy(),
            "subtract": SubtractOperationStrategy(),
            "multiply": MultiplyOperationStrategy(),
            "divide": DivideOperationStrategy(),
        }
        self.strategies.update(self.load_plugins())

    def load_plugins(self):
        plugins = {}
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        if not os.path.exists(plugins_dir):
            self.logger.warning("Plugins directory does not exist.")
            return plugins

        for module in os.listdir(plugins_dir):
            if module == '__init__.py' or module[-3:] != '.py':
                continue
            module_name = module[:-3]
            try:
                module_path = f'.plugins.{module_name}'
                plugin_module = importlib.import_module(module_path, package='App')
                for item in dir(plugin_module):
                    obj = getattr(plugin_module, item)
                    if isinstance(obj, type) and issubclass(obj, OperationStrategy) and obj is not OperationStrategy:
                        plugin_name = obj.__name__
                        plugins[plugin_name.lower()] = obj()
                        self.logger.info(f"Loaded plugin: {plugin_name}")
            except Exception as e:
                self.logger.error(f"Failed to load plugin {module_name}: {e}")

        return plugins



    def display_menu(self):
        print("\nAvailable Commands:")
        for command in self.strategies.keys():
            print(f" - {command}")
        print(" - history: View calculation history")
        print(" - quit: Exit the calculator")
        print(" - help: Show this menu again\n")
        print("Enter 'command operands' (e.g., 'add 1 2') to perform a calculation, or use one of the above commands.")

    def run(self):
        print("Welcome to the Advance Calculator")
        self.display_menu()

        while True:
            try:
                user_input = input("calc> ").strip().lower()
                if user_input == "quit":
                    self.logger.info("Calculator app terminated.")
                    break
                elif user_input == "history":
                    self.history_manager.show_history()
                elif user_input == "help":
                    self.display_menu()
                else:
                    parts = user_input.split()
                    command, operands = parts[0], parts[1:]
                    operands = list(map(float, operands))
                    
                    if command in self.strategies:
                        calculator = CalculatorContext(self.strategies[command], self.history_manager)
                        result = calculator.execute_operation(*operands)
                        print(f"Result: {result}")
                    else:
                        print("Unknown command. Type 'help' to see available commands.")
            except Exception as e:
                self.logger.error(f"An error occurred: {e}")
                print("An error occurred. Please try again.")
