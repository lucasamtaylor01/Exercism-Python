def factors(value):
    i = 2
    prime_list = []
    while value != 1:
        if value % i == 0:
            value = value // i
            prime_list.append(i)
        else:
            i+=1
        
    return prime_list
