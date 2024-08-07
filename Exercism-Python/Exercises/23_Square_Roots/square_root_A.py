def factorization(n):
    factorization_list = []
    i = 2
    while n != 1:
        if n % i == 0:
            factorization_list.append(i)
            n = n // i
        else:
            i+=1

    return factorization_list

def perfect_square(n):
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
    factors = factorization(n)
    root_factors = []
    for i in range(len(factors)):
        if i % 2 == 0:
            root_factors.append(factors[i])

    root = 1
    for i in range(len(root_factors)):
        root*=root_factors[i]
    
    return root

def foward_perfect_square(n):
    i = n+1
    while True:
        if perfect_square(i):
            return i
        else:
            i+=1

def previous_perfect_square(n):
    i = n-1
    while True:
        if perfect_square(i):
            return i
        else:
            i-=1

def square_root(n):
    foward_square = perfect_square_root(foward_perfect_square(n))
    previuos_square = perfect_square_root(previous_perfect_square(n))

    a = (foward_square + previuos_square) /2
    b = n / a
    counter = 0
    while counter < 10**4:
        a = (a+b)/2
        b = n / a
        counter+=1
    return b

        
print(square_root(121))