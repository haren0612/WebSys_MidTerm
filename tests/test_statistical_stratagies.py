import pytest
from App.stratagies.statistical_stratagies import MeanOperationStrategy, MedianOperationStrategy, StdDevOperationStrategy

def test_mean_operation():
    strategy = MeanOperationStrategy()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 1, 1, 1, 1) == 1

def test_median_operation():
    strategy = MedianOperationStrategy()
    assert strategy.execute(1, 2, 3, 4, 5) == 3
    assert strategy.execute(1, 2, 3, 4, 5, 6) == 3.5

def test_std_dev_operation():
    strategy = StdDevOperationStrategy()
    assert strategy.execute(1, 2, 3, 4, 5) == pytest.approx(1.5811388300841898)
    with pytest.raises(ValueError):
        strategy.execute(1)  # Assuming your StdDevOperationStrategy raises a ValueError for insufficient operands

def test_std_dev_operation_with_insufficient_data():
    strategy = StdDevOperationStrategy()
    with pytest.raises(ValueError):
        strategy.execute(1)  # Only one number provided