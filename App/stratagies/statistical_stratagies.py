from statistics import mean, median, stdev

from App.stratagies.base_strategy import OperationStrategy

class MeanOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        return mean(operands)

class MedianOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        return median(operands)

class StdDevOperationStrategy(OperationStrategy):
    def execute(self, *operands):
        if len(operands) < 2:
            raise ValueError("Standard deviation requires at least two operands.")
        return stdev(operands)
