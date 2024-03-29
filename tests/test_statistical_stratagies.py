import pytest
from App.stratagies.statistical_stratagies import MeanOperation, MedianOperation, StdDevOperation

def test_mean_operation():
    strategy = MeanOperation()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 1, 1, 1, 1) == 1

def test_median_operation():
    strategy = MedianOperation()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 2, 3, 4, 5, 6) == 3.5

def test_std_dev_operation():
    strategy = StdDevOperation()
    assert strategy.execute(1, 2, 3, 4, 5) == pytest.approx(1.5811388300841898)
    with pytest.raises(ValueError):
        strategy.execute(1)  # Assuming your StdDevOperationStrategy raises a ValueError for insufficient operands

def test_std_dev_operation_with_insufficient_data():
    strategy = StdDevOperation()
    with pytest.raises(ValueError):
        strategy.execute(1)  # Only one number provided