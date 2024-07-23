def square(number):
    if 1 <= number <= 64:
        grains = 2**(number-1)
        return grains
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    sum = 0
    for i in range(1, 65):
        sum+=square(i)

    return sum
