import time
from math import sqrt,floor

def criba(x):
    limiteSuperior = floor(sqrt(x))
    matriz = [True for _ in range(x+1)]
    matriz[0] = False
    matriz[1] = False
    for i in range(2, limiteSuperior + 1):
        if not matriz[i]:
            continue
        k = 2
        while k*i < len(matriz): 
            matriz[i*k] = False
            k = k+1
    return [x for x in range(len(matriz)) if matriz[x]]

def obtenerListaDeDigitosDeNumero(x):
    lista = []
    while x > 0:
        lista.append(x % 10)
        x = x // 10
    lista.reverse()
    return lista

def obtenerNumeroDeLista(x):
    res = 0
    for i in range(len(x)):
        res = res + x[i] * (10**(len(x)-1-i))
    return res

primos = criba(1000000)
primosSet = set(primos)
res = 0

for primo in primos:
    listaPrimo = obtenerListaDeDigitosDeNumero(primo)
    esRespuesta = True
    for i in range(len(listaPrimo) - 1):
        listaPrimo.append(listaPrimo.pop(0))
        numero = obtenerNumeroDeLista(listaPrimo)
        if numero not in primosSet:
            esRespuesta = False
            break
    if esRespuesta:
        res = res + 1

print(res)
