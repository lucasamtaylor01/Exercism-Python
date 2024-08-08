import math

def prime(number):
    """
    Returns the nth prime number.
    
    :param number: The position of the desired prime number.
    :return: The nth prime number.
    :raises ValueError: If the position of the prime number is less than 1.
    """
    if number == 0:
        raise ValueError("There is no zeroth prime")
    
    i = 2
    prime_counter = 0
    
    while True:
        if isprime(i):
            prime_counter += 1
            if prime_counter == number:
                return i
        i += 1
    
def isprime(number):
    """
    Checks if a number is prime.
    
    :param number: The number to be checked.
    :return: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
