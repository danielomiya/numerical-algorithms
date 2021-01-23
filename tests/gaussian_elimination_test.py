import pytest
from numerical_algorithms.gaussian_elimination import gaussian_elimination


@pytest.mark.parametrize(
    "matrix,expected",
    [
        (
            [  # example
                [1, 1, 0, 3, 4],
                [0, -1, -1, -5, -7],
                [0, 0, 3, 13, 13],
                [0, 0, 0, -13, -13],
            ],
            [-1, 2, 0, 1],
        ),
        (
            [  # 3.a
                [1, -1, 3, 2],
                [3, -3, 1, -1],
                [1, 1, 0, 3],
            ],
            [1.1875, 1.8125, 0.875],
        ),
        (
            [  # 3.b
                [2, -1.5, 3, 1],
                [-1, 0, 2, 3],
                [4, -4.5, 5, 1],
            ],
            [-1, 0, 1],
        ),
        (
            [  # 3.c
                [2, 0, 0, 0, 3],
                [1, 1.5, 0, 0, 4.5],
                [0, -3, 0.5, 0, -6.6],
                [2, -2, 1, 1, 0.8],
            ],
            [1.5, 2, -1.2, 3],
        ),
    ],
)
def test_main(matrix, expected):
    result = gaussian_elimination(matrix)

    assert pytest.approx(expected) == result


def test_error():
    matrix = [  # 3.d
        [1, 1, 0, 1, 2],
        [2, 1, -1, 1, 1],
        [4, -1, -2, 2, 0],
        [3, -1, -1, 2, -3],
    ]

    with pytest.raises(ArithmeticError) as exc_info:
        gaussian_elimination(matrix)

    assert str(exc_info.value) == "no unique solution exists"
