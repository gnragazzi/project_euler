from math import floor, sqrt
from functools import reduce

def divisores(n):
    divisores = {1,n}
    limite_superior = floor(sqrt(n))
    for i in range(1,limite_superior+1):
        if(n%i==0):
            divisores.add(i)
            divisores.add(n//i)
    return divisores

def suma_divisores(n):
    div = divisores(n)
    return reduce(lambda acc, x: acc + x, div)

def lista_amicables_bajo_n(n):
    se_evalua = [True for x in range(1,n+2)]
    lista_amicables = []
    for i in range(220,n+1):
        if(se_evalua[i]):
            se_evalua[i] = False
            x = suma_divisores(i)
            supuesto_par = x-i
            if(supuesto_par <= n and se_evalua[supuesto_par] and x == suma_divisores(x-i)):
                lista_amicables.append(i)                                
                lista_amicables.append(supuesto_par)
                se_evalua[supuesto_par] = False
    return lista_amicables

def suma_lista_amicables_bajo_n(n):
    return reduce(lambda acc, x: acc+x,lista_amicables_bajo_n(n))

