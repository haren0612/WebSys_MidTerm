from ..stratagies.base_stratagy import OperationStrategy

class Square(OperationStrategy):
    def execute(self, *operands):
        if len(operands) != 1:
            raise ValueError("Square plugin requires exactly 1 operand")
        return operands[0] ** 2

