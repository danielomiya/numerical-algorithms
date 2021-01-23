from typing import List


def jacobi_method(
    matrix: List[List[float]],
    max_iter: int = 100,
    tolerance: float = 1e-10,
    roots: List[float] = None,
) -> List[float]:
    """
    Given a system of equations, returns an approximation of the unknowns

    :param matrix: system of equations
    :param max_iter: maximum number of iterations, defaults to 100
    :param tolerance: acceptable tolerance for the approx, defaults to 1e-10
    :param roots: approx of the roots, defaults to None
    :raises ArithmeticError: when unable to find a result with the defined constraints
    :return: approximation the unknowns
    """
    number_equations = len(matrix)

    if roots is None:
        roots = [0] * number_equations
        return jacobi_method(matrix, max_iter - 1, tolerance, roots)

    approx = [0] * number_equations

    for i in range(number_equations):
        summation = 0

        for j in range(number_equations):
            summation += matrix[i][j] * roots[j]
        summation -= matrix[i][i] * roots[i]

        approx[i] = (matrix[i][number_equations] - summation) / matrix[i][i]

    if all(abs(a - r) < tolerance for a, r in zip(approx, roots)):
        return approx

    if max_iter > 0:
        return jacobi_method(matrix, max_iter - 1, tolerance, approx)

    raise ArithmeticError(
        "unable to find an approximation with the defined constraints"
    )
