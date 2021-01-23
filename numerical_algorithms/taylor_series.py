from typing import Optional


def taylor_series(x: int, max_iter: Optional[int] = 10) -> float:
    """Calculates an approximation of e^x using an expansion of the Taylor series.

    :param x: exponent of e
    :param max_iter: max num of iterations, defaults to 10
    :return: e^x
    """
    result = 1
    fat = 1
    power = 1

    for i in range(1, max_iter + 1):
        fat *= i
        power *= x
        result += power / fat

    return result
