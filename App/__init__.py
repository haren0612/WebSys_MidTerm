import logging
from App.CalculatorContext import CalculatorContext
from App.HistoryManager import HistoryManager
from App.stratagies.statistical_stratagies import MeanOperation, MedianOperation, StdDevOperation
from .stratagies.arithmetic_stratagies import Addition, Subtraction, Multiplication, Division
from .utils.plugin_loader import load_plugins

class CalculatorApp:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.history_manager = HistoryManager()
        self.strategies = {
            "add": Addition(),
            "subtract": Subtraction(),
            "multiply": Multiplication(),
            "divide": Division(),
            "mean": MeanOperation(),
            "median": MedianOperation(),
            "stddev": StdDevOperation(),
        }
        self.strategies.update(load_plugins())


    def display_menu(self):
        print("\nAvailable Commands:")
        for command in self.strategies.keys():
            print(f" - {command}")
        print(" - history: View calculation history")
        print(" - quit: Exit the calculator")
        print(" - help: Show this menu again\n")
        print("Enter 'command operands' (e.g., 'add 1 2') to perform a calculation, or use one of the above commands.")


    def run(self):
        print("Welcome to the Advanced Calculator")
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
                    command, operands_str = parts[0], parts[1:]
                    
                    if command not in self.strategies:
                        print("Unknown command. Type 'help' to see available commands.")
                        continue
                    
                    try:
                        operands = list(map(float, operands_str))
                    except ValueError:
                        print("Error: All operands must be numeric.")
                        continue
                    
                    calculator = CalculatorContext(self.strategies[command], self.history_manager)
                    result = calculator.execute_operation(*operands)
                    print(f"Result: {result}")
                    
            except ValueError as ve:
                # Specific known errors, e.g., "Cannot divide by zero."
                self.logger.warning(f"Operation warning: {ve}")
                print(f"Warning: {ve}")
            except Exception as e:
                # Catch-all for unexpected errors
                self.logger.error(f"Unexpected error occurred: {e}", exc_info=True)
                print("An unexpected error occurred. Please try again.")

