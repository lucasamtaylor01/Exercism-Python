def square_of_sum(number):
    """
    Calculate the square of the sum of the first `number` natural numbers.

    :param number: An integer representing the upper limit of the range.
    :return: The square of the sum of the first `number` natural numbers.
    """
    total_sum = 0
    for i in range(number + 1):
        total_sum += i
    return total_sum ** 2


def sum_of_squares(number):
    """
    Calculate the sum of the squares of the first `number` natural numbers.

    :param number: An integer representing the upper limit of the range.
    :return: The sum of the squares of the first `number` natural numbers.
    """
    total_sum = 0
    for i in range(number + 1):
        total_sum += i ** 2
    return total_sum


def difference_of_squares(number):
    """
    Calculate the difference between the square of the sum and the sum of the squares of the first `number` natural numbers.

    :param number: An integer representing the upper limit of the range.
    :return: The difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
