import pytest
from numerical_algorithms.jacobi_method import jacobi_method


@pytest.mark.parametrize(
    "matrix,expected",
    [
        (
            [  # example 1
                [10, -1, 2, 0, 6],
                [-1, 11, -1, 3, 25],
                [2, -1, 10, -1, -11],
                [0, 3, -1, 8, 15],
            ],
            [1, 2, -1, 1],
        ),
        (
            [  # example 2
                [2, 1, 2],
                [1, -2, -2],
            ],
            [0.4, 1.2],
        ),
        (
            [  # a
                [3, -1, 1, 1],
                [3, 6, 2, 0],
                [3, 3, 7, 4],
            ],
            [2 / 57, -9 / 38, 25 / 38],
        ),
        (
            [  # b
                [10, -1, 0, 9],
                [-1, 10, -2, 7],
                [0, -2, 10, 6],
            ],
            [473 / 475, 91 / 95, 376 / 475],
        ),
        (
            [  # c
                [10, 5, 0, 0, 6],
                [5, 10, -4, 0, 25],
                [0, -4, 8, -1, -11],
                [0, 0, -1, 5, -11],
            ],
            [-339 / 425, 1188 / 425, -22 / 85, -957 / 425],
        ),
        (
            [  # d
                [4, 1, 1, 0, 1, 6],
                [-1, -3, 1, 1, 0, 6],
                [2, 1, 5, -1, -1, 6],
                [-1, -1, -1, 4, 0, 6],
                [0, 2, -1, 1, 4, 6],
            ],
            [306 / 389, -390 / 389, 726 / 389, 744 / 389, 774 / 389],
        ),
    ],
)
def test_main(matrix, expected):
    result = jacobi_method(matrix)
    assert pytest.approx(expected) == result
