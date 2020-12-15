from typing import List, Optional


def calc_error(avg_point: float, number: int) -> float:
    """[summary]

    Args:
        avg_point (float): [description]
        number (int): [description]

    Returns:
        float: [description]
    """
    return avg_point**2 - number


def avg(*args: List[float]) -> float:
    """[summary]

    Returns:
        float: [description]
    """
    return sum(args)/len(args)


def babylonian_sqrt(number: float, lower_lim: Optional[float] = None, upper_lim: Optional[float] = None, rounds: Optional[int] = 10) -> float:
    """[summary]

    Args:
        number (float): [description]
        lower_lim (Optional[float], optional): [description]. Defaults to None.
        upper_lim (Optional[float], optional): [description]. Defaults to None.
        rounds (Optional[int], optional): [description]. Defaults to 10.

    Raises:
        ArithmeticError: [description]

    Returns:
        float: [description]
    """
    if number == 0:
        # square root of 0 is 0
        return .0

    if number < 0:
        # there is not sqrt for negative nums
        raise ArithmeticError('there is no sqrt for negative numbers')

    if lower_lim is None and upper_lim is None:
        # first approx
        i = 0
        while not i**2 <= number < (i+1)**2:
            i += 1

        return babylonian_sqrt(number, i, i+1, rounds-1)

    err = calc_error(lower_lim, number)

    if err == 0:
        # early return for perfect squares
        return lower_lim

    avg_point = avg(upper_lim, lower_lim)

    if rounds <= 0:
        # limit of rounds to keep approximating
        return avg_point

    err = calc_error(avg_point, number)

    if err > 0:
        # if err > 0, get a smaller num between lower_lim and avg_point
        return babylonian_sqrt(number, lower_lim, avg_point, rounds-1)

    # else the approximation is between avg_point and upper_lim
    return babylonian_sqrt(number, avg_point, upper_lim, rounds-1)
