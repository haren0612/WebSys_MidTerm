import os
import logging
import importlib
from App.CalculatorContext import CalculatorContext
from App.HistoryManager import HistoryManager
from App.stratagies.statistical_stratagies import MeanOperationStrategy, MedianOperationStrategy, StdDevOperationStrategy
from .stratagies.arithmetic_stratagies import AddOperationStrategy, SubtractOperationStrategy, MultiplyOperationStrategy, DivideOperationStrategy
from .utils.plugin_loader import load_plugins

class CalculatorApp:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.history_manager = HistoryManager()
        self.strategies = {
            "add": AddOperationStrategy(),
            "subtract": SubtractOperationStrategy(),
            "multiply": MultiplyOperationStrategy(),
            "divide": DivideOperationStrategy(),
            "mean": MeanOperationStrategy(),  # Add the mean strategy
            "median": MedianOperationStrategy(),  # Add the median strategy
            "stddev": StdDevOperationStrategy(),  # Add the standard deviation strategy
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
