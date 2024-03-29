from ..stratagies.base_stratagy import OperationStrategy

class Power(OperationStrategy):
    def execute(self, *operands):
        if len(operands) != 2:
            return "Error: power operation requires exactly two operands."
        base, exponent = operands
        return base ** exponent
