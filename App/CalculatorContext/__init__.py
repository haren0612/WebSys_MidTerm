class CalculatorContext:
    def __init__(self, strategy, history_manager):
        self._strategy = strategy
        self.history_manager = history_manager

    def execute_operation(self, *operands):
        # Execute the operation using the provided strategy
        result = self._strategy.execute(*operands)
        
        # Prepare details for history logging
        operation_name = self._strategy.__class__.__name__
        
        # Convert operands to a format suitable for storage/display
        operands_str = ', '.join(map(str, operands))
        
        # Add an entry to the history log
        # Adjusted to match the updated add_entry method signature
        self.history_manager.add_entry(operation_name, operands_str, result)
        
        # Optionally, if immediate saving to CSV is desired
        # self.history_manager.save_history()
        
        return result
