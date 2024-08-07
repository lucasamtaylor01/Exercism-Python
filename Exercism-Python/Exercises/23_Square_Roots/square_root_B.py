def factorization(n):
    factorization_list = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factorization_list.append(i)
            n //= i
        i += 1
    if n > 1:
        factorization_list.append(n)
    return factorization_list

def perfect_square(n):
    factors = factorization(n)
    factor_counts = {}
    
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
    
    for count in factor_counts.values():
        if count % 2 != 0:
            return False
    return True

def perfect_square_root(n):
    factors = factorization(n)
    factor_counts = {}
    
    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1
    
    root = 1
    for factor, count in factor_counts.items():
        root *= factor ** (count // 2)
    
    return root

def next_perfect_square(n):
    i = n + 1
    while not perfect_square(i):
        i += 1
    return i

def previous_perfect_square(n):
    i = n - 1
    while not perfect_square(i):
        i -= 1
    return i

def square_root(n):
    forward_square = perfect_square_root(next_perfect_square(n))
    previous_square = perfect_square_root(previous_perfect_square(n))

    a = (forward_square + previous_square) / 2
    b = n / a
    for _ in range(10**4):
        a = (a + b) / 2
        b = n / a