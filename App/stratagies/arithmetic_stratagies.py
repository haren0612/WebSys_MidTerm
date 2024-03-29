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
    def execute(self, *operands):
        if len(operands) == 1:
            return 1 / operands[0]
        else:
            if operands[1] == 0:
                raise ZeroDivisionError
            return operands[0] / operands[1]