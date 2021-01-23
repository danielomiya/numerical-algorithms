from typing import Callable, Optional


def bisection_method(
    point_a: float,
    point_b: float,
    function: Callable[[float], float],
    tolerance: Optional[float] = 1e-10,
    max_iter: Optional[int] = 100,
) -> float:
    """[summary]

    Args:
        point_a (float): [description]
        point_b (float): [description]
        function (Callable[[float], float]): [description]
        tolerance (Optional[float], optional): [description]. Defaults to 1e-10.
        max_iter (Optional[int], optional): [description]. Defaults to 100.

    Returns:
        float: [description]
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
