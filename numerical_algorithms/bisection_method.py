from typing import Callable


def bisection_method(
    point_a: float,
    point_b: float,
    function: Callable[[float], float],
    tolerance: float = 1e-10,
    max_iter: int = 100,
) -> float:
    """
    Calculates the root of a continuous function using bisection method

    :param point_a: point A of bisection
    :param point_b: point B of bisection
    :param function: function whose root we're looking for
    :param tolerance: acceptable tolerance for the approx, defaults to 1e-10
    :param max_iter: maximum number of iterations, defaults to 100
    :raises ArithmeticError: when unable to solve with given constraints
    :return: root of function
    """
    i = 0
    fa = function(point_a)

    while i < max_iter:
        point_p = point_a + (point_b - point_a) / 2
        fp = function(point_p)

        if fp == 0 or (point_b - point_a) / 2 < tolerance:
            return point_p

        if fa * fp > 0:
            point_a = point_p
            fa = fp
        else:
            point_b = point_p

        i += 1

    raise ArithmeticError("could not solve with given constraints")
