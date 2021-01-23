from typing import List


def _calc_error(avg_point: float, number: int) -> float:
    return avg_point ** 2 - number


def _avg(*args: List[float]) -> float:
    return sum(args) / len(args)


def babylonian_sqrt(
    number: float,
    lower_lim: float = None,
    upper_lim: float = None,
    rounds: int = 10,
) -> float:
    """
    Calculates a square root using babylonian algorithm.

    :param number: number whose square root we're calculating
    :param lower_lim: approx lower limit, defaults to None
    :param upper_lim: approx upper limit, defaults to None
    :param rounds: max num of iterations, defaults to 10
    :raises ArithmeticError: when number is negative
    :return: square root of number
    """
    if number == 0:
        # square root of 0 is 0
        return 0.0

    if number < 0:
        # there is not sqrt for negative nums
        raise ArithmeticError("there is no sqrt for negative numbers")

    if lower_lim is None and upper_lim is None:
        # first approx
        i = 0
        while not i ** 2 <= number < (i + 1) ** 2:
            i += 1

        return babylonian_sqrt(number, i, i + 1, rounds - 1)

    err = _calc_error(lower_lim, number)

    if err == 0:
        # early return for perfect squares
        return lower_lim

    avg_point = _avg(upper_lim, lower_lim)

    if rounds <= 0:
        # limit of rounds to keep approximating
        return avg_point

    err = _calc_error(avg_point, number)

    if err > 0:
        # if err > 0, get a smaller num between lower_lim and avg_point
        return babylonian_sqrt(number, lower_lim, avg_point, rounds - 1)

    # else the approximation is between avg_point and upper_lim
    return babylonian_sqrt(number, avg_point, upper_lim, rounds - 1)
