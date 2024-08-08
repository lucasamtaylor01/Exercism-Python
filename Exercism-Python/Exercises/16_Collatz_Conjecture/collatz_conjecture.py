def steps(number):
    """
    Calculate the number of steps to reach 1 in the Collatz sequence.

    The Collatz sequence is defined as follows:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    - Repeat the process until the number becomes 1.

    :param number: A positive integer to start the Collatz sequence.
    :return: The number of steps to reach 1.
    :raises ValueError: If the input number is not a positive integer.
    """
    if number > 0:
        i = 1
        while number != 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = number * 3 + 1
            i += 1
        
        return i - 1
    else:
        raise ValueError("Only positive integers are allowed")
