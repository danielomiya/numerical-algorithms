from typing import List


def _validate_system_of_equations(matrix: List[List[float]]) -> None:
    equations_len = len(matrix)
    line_len = equations_len + 1

    if equations_len >= 1 and all(len(s) == line_len for s in matrix):
        return

    raise ArithmeticError("malformed system of equations")


def gaussian_elimination(matrix: List[List[float]]) -> List[float]:
    """
    Given an system of equations, calculates the unknowns using Gaussian method

    :param matrix: system of equations
    :raises ArithmeticError: when the input is not valid
    :return: values of the unknowns
    """
    _validate_system_of_equations(matrix)

    number_equations = len(matrix)
    unknowns = [None] * number_equations

    # elimination process
    for i in range(number_equations - 1):  # iter rows
        # search for pivot index in column
        pivot = min(
            (
                p
                for p, row in enumerate(matrix)
                if row[i] != 0 and i <= p < number_equations
            ),
            default=None,
        )

        if pivot is None:
            raise ArithmeticError("no unique solution exists")

        if pivot != i:
            # if pivot is not current row, swipe rows
            matrix[pivot], matrix[i] = matrix[i], matrix[pivot]

        for j in range(i + 1, number_equations):
            m = matrix[j][i] / matrix[i][i]  # pylint: disable=invalid-name
            subtrahend = [a * m for a in matrix[i]]

            # Ej = Ej - m * Ei
            matrix[j] = [m - s for m, s in zip(matrix[j], subtrahend)]

    if matrix[number_equations - 1][number_equations - 1] == 0:
        raise ArithmeticError("no unique solution exists")

    # backward substitution
    for i in reversed(range(number_equations)):
        summ = 0

        for j in range(i + 1, number_equations):
            summ += matrix[i][j] * unknowns[j]

        right = matrix[i][number_equations]  # right side of equation
        numerator = right - summ
        denominator = matrix[i][i]

        unknowns[i] = numerator / denominator

    return unknowns
