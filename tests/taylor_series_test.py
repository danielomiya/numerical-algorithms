import pytest
from taylor_series import taylor_series

def test_main():
    result = taylor_series(2, 15)
    assert result == pytest.approx(7.38905, 1e-4)
