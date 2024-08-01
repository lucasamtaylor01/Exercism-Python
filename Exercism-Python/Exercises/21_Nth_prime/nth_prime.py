import math

def prime(number):
    """
    Retorna o enésimo número primo.
    
    :param number: A posição do número primo desejado.
    :return: O enésimo número primo.
    """
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
    Verifica se um número é primo.
    
    :param number: O número a ser verificado.
    :return: True se o número for primo, False caso contrário.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True