import math

'''
def esPrimo(x):
    if(x==1):
        return False
    divisor = 2
    limite_superior= math.floor(math.sqrt(x))
    while divisor <= limite_superior:
        if(x % divisor == 0):
            return False
        else:
            divisor += 1
    return True
'''
def esPrimo(x):
    if(x==1):
        return False
    if(x==2 or x == 3):
        return True
    if(x%2==0 or x % 3 == 0):
        return False
    limite_superior= math.floor(math.sqrt(x))
    factor = 6 #por lo visto en https://projecteuler.net/overview=0007, todos los primo > 3 puede ser expresado como 6k ± 1, con k∈N
    while(factor - 1 <= limite_superior):
        #print(f"Limite: {limite_superior}, factor: {factor}")
        if(x % (factor - 1)==0 or x % (factor + 1)==0):
            return False
        factor += 6
    return True
