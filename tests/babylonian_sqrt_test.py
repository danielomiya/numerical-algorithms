import pytest
from numerical_algorithms.babylonian_sqrt import babylonian_sqrt


def test_main():
    sqrt = babylonian_sqrt(2, rounds=25)
    assert pytest.approx(1.4142, rel=1e-4) == sqrt
