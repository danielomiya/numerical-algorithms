from typing import Optional

def taylor_series(x: int, n: Optional[int] = 10) -> float:
    """Calculates an approximation of e^x using an expansion of the Taylor series.

    Args:
        x (int): exponent of e.
        n (int, optional): max num of iterations. Defaults to 10.
    
    Returns:
        float: e^x
    """
    result = 1
    fat = 1
    power = 1

    for i in range(1, n+1):
        fat *= i
        power *= x
        result += power/fat

    return result
