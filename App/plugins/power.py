from App.utils.log_wrapper import log_operation
from ..stratagies.base_strategy import OperationStrategy

class Power(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        if len(operands) != 2:
            return "Error: power operation requires exactly two operands."
        base, exponent = operands
        return base ** exponent
