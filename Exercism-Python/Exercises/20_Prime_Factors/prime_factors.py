def factors(value):
    """
    Compute the prime factors of a given integer.

    The function returns a list of prime numbers that, when multiplied together, result in the original integer.

    :param value: An integer to factorize into prime factors.
    :return: A list of prime factors of the given integer.
    """
    i = 2
    prime_list = []
    while value != 1:
        if value % i == 0:
            value = value // i
            prime_list.append(i)
        else:
            i += 1
        
    return prime_list
