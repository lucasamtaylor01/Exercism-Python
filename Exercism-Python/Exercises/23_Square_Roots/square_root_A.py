def factorization(n):
    """
    Perform the prime factorization of a given integer.

    :param n: An integer to be factorized.
    :return: A list of prime factors of the given integer.
    """
    factorization_list = []
    i = 2
    while n != 1:
        if n % i == 0:
            factorization_list.append(i)
            n = n // i
        else:
            i += 1

    return factorization_list

def perfect_square(n):
    """
    Determine if a given integer is a perfect square.

    :param n: An integer to check for being a perfect square.
    :return: True if the integer is a perfect square, False otherwise.
    """
    factors = factorization(n)

    i = 0
    counter = 1
    
    while i < len(factors):
        if i + 1 < len(factors) and factors[i] == factors[i + 1]:
            counter += 1
        else:
            if counter % 2 != 0:
                return False
            counter = 1
        i += 1
    
    return True

def perfect_square_root(n):
    """
    Calculate the square root of a perfect square.

    :param n: An integer that is a perfect square.
    :return: The integer square root of the perfect square.
    """
    factors = factorization(n)
    root_factors = []
    for i in range(len(factors)):
        if i % 2 == 0:
            root_factors.append(factors[i])

    root = 1
    for i in range(len(root_factors)):
        root *= root_factors[i]
    
    return root

def foward_perfect_square(n):
    """
    Find the next perfect square greater than a given integer.

    :param n: An integer to find the next perfect square.
    :return: The next perfect square greater than the given integer.
    """
    i = n + 1
    while True:
        if perfect_square(i):
            return i
        else:
            i += 1

def previous_perfect_square(n):
    """
    Find the previous perfect square less than a given integer.

    :param n: An integer to find the previous perfect square.
    :return: The previous perfect square less than the given integer.
    """
    i = n - 1
    while True:
        if perfect_square(i):
            return i
        else:
            i -= 1

def square_root(n):
    """
    Approximate the square root of a given integer.

    :param n: An integer to approximate the square root.
    :return: The approximate square root of the given integer.
    """
    foward_square = perfect_square_root(foward_perfect_square(n))
    previous_square = perfect_square_root(previous_perfect_square(n))

    a = (foward_square + previous_square) / 2
    b = n / a
    counter = 0
    while counter < 10**4:
        a = (a + b) / 2
        b = n / a
        counter += 1
    return b