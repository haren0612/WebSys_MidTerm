import pytest
from ..App.strategies.arithmetic_strategies import AddOperationStrategy, DivideOperationStrategy, MultiplyOperationStrategy, SubtractOperationStrategy

def test_add_operation():
    strategy = AddOperationStrategy()
    assert strategy.execute(1, 2) == 3

def test_subtract_operation():
    strategy = SubtractOperationStrategy()
    assert strategy.execute(5, 3) == 2

def test_multiply_operation():
    strategy = MultiplyOperationStrategy()
    assert strategy.execute(5, 3) == 15

def test_divide_operation():
    strategy = DivideOperationStrategy()
    assert strategy.execute(6, 3) == 2

def divide_by_zero():
    strategy = DivideOperationStrategy()
    with pytest.raises(ZeroDivisionError):
        strategy.execute(6, 0)

