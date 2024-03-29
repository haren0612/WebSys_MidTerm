from App.utils.log_wrapper import log_operation
from ..stratagies.base_strategy import OperationStrategy

class Square(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        if len(operands) != 1:
            raise ValueError("Square plugin requires exactly 1 operand")
        return operands[0] ** 2

