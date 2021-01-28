def taylor_series(x: int, max_iter: int = 100) -> float:
    """
    Calculates an approximation of e :superscript:`x`
    using an expansion of the Taylor series.

    :param x: exponent of e
    :param max_iter: max num of iterations, defaults to 100
    :return: e :superscript:`x`
    """
    result = 1
    fat = 1
    power = 1

    for i in range(1, max_iter + 1):
        fat *= i
        power *= x
        result += power / fat

    return result
