def is_armstrong_number(number):
    div = number
    dec = decimals(number)
    lista = []
    for i in range(dec-1, -1 , -1):
        aux = div // 10**i 
        div = div % 10**i
        lista.append(aux)
    
    sm =0
    for i in range(len(lista)):
        sm+=lista[i]**dec
    
    if sm == number:
        return True
    else:
        return False
        
def decimals(number):
    decimals = 0
    while number != 0: 
        number = number // 10
        decimals+=1
    
    return decimals
