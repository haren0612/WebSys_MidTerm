class CalculatorContext:
    def __init__(self, strategy, history_manager):
        self._strategy = strategy
        self.history_manager = history_manager

    def execute_operation(self, *operands):
        result = self._strategy.execute(*operands)
        operation_desc = f"{self._strategy.__class__.__name__} with {operands} = {result}"
        self.history_manager.add_record(operation_desc)
        return result
