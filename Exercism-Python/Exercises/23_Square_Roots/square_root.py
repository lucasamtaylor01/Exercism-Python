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
    error = 0.0000001
    a = (previous_perfect_square(n)+ foward_perfect_square(n))/2
    b = n / a

    while True:
        a = a+b/2
        b = n / a
        print(a, b)
        if abs(b**2 - n) < error:
            return b
        
print(square_root(4))