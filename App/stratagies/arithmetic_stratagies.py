from .base_strategy import OperationStrategy

class AddOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        return sum(operands)
    
class SubtractOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        result = operands[0]
        for operand in operands[1:]:
            result -= operand
        return result
    
class MultiplyOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        result = 1
        for operand in operands:
            result *= operand
        return result

class DivideOperationStrategy(OperationStrategy):
    def execute(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2
