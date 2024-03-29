from App.utils.log_wrapper import log_operation
from .base_strategy import OperationStrategy


class Addition(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)
        return sum(operands)
    
class Subtraction(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)
        result = operands[0]
        for operand in operands[1:]:
            result -= operand
        return result
    
class Multiplication(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)
        result = 1
        for operand in operands:
            result *= operand
        return result

class Division(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)
        operand1, operand2 = operands
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2
