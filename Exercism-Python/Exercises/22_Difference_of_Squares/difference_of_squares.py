def square_of_sum(number):
    total_sum = 0
    for i in range(number + 1):
        total_sum += i
    return total_sum**2


def sum_of_squares(number):
    total_sum = 0
    for i in range(number + 1):
        total_sum += i**2
    return total_sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
