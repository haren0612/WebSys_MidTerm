import pytest
from App.stratagies.arithmetic_stratagies import AddOperationStrategy, SubtractOperationStrategy, MultiplyOperationStrategy, DivideOperationStrategy

def test_add_operation():
    strategy = AddOperationStrategy()
    assert strategy.execute(1, 2) == 3
    assert strategy.execute(-1, -2) == -3
    assert strategy.execute(0, 0) == 0

def test_subtract_operation():
    strategy = SubtractOperationStrategy()
    assert strategy.execute(5, 3) == 2
    assert strategy.execute(-1, -2) == 1
    assert strategy.execute(0, 0) == 0

def test_multiply_operation():
    strategy = MultiplyOperationStrategy()
    assert strategy.execute(2, 3) == 6
    assert strategy.execute(-1, -2) == 2
    assert strategy.execute(0, 10) == 0

def test_divide_operation():
    strategy = DivideOperationStrategy()
    assert strategy.execute(6, 3) == 2
    assert strategy.execute(-4, -2) == 2
    # Testing division by zero
    with pytest.raises(ValueError) as e:
        strategy.execute(1, 0)
    assert str(e.value) == "Cannot divide by zero."

def test_divide_operation_by_zero():
    strategy = DivideOperationStrategy()
    with pytest.raises(ValueError) as exc_info:
        strategy.execute(10, 0)
    assert "cannot divide by zero" in str(exc_info.value).lower()

def test_add_operation_with_invalid_inputs():
    strategy = AddOperationStrategy()
    with pytest.raises(TypeError):
        strategy.execute("a", 2)

def test_subtract_operation_with_invalid_inputs():
    strategy = SubtractOperationStrategy()
    with pytest.raises(TypeError):
        strategy.execute(1, "b")