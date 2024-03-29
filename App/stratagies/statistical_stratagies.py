from statistics import mean, median, stdev
from App.stratagies.base_strategy import OperationStrategy  # Corrected the typo in the path
from App.utils.log_wrapper import log_operation

class MeanOperation(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)  # Validate input before performing the operation
        return mean(operands)

class MedianOperation(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)  # Validate input before performing the operation
        return median(operands)

class StdDevOperation(OperationStrategy):
    @log_operation
    def execute(self, *operands):
        self.validate_operands(*operands)  # Validate input before performing the operation
        if len(operands) < 2:
            raise ValueError("Standard deviation requires at least two operands.")
        return stdev(operands)
