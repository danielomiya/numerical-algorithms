from typing import Optional


def taylor_series(x: int, max_iter: Optional[int] = 10) -> float:  # pylint: disable=C0103
    """Calculates an approximation of e^x using an expansion of the Taylor series.

    Args:
        x (int): exponent of e.
        max_iter (int, optional): max num of iterations. Defaults to 10.

    Returns:
        float: e^x
    """
    result = 1
    fat = 1
    power = 1

    for i in range(1, max_iter+1):
        fat *= i
        power *= x
        result += power/fat

    return result
