def square(number):
    """
    Calculate the number of grains of wheat on a given square of a chessboard.

    :param number: The square number (must be between 1 and 64).
    :return: The number of grains on the given square.
    :raises ValueError: If the square number is not between 1 and 64.
    """
    if 1 <= number <= 64:
        grains = 2**(number-1)
        return grains
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    """
    Calculate the total number of grains of wheat on a chessboard.

    :return: The total number of grains on all 64 squares.
    """
    sum = 0
    for i in range(1, 65):
        sum += square(i)

    return sum
