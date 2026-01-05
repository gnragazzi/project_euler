import time
from math import sqrt,floor
from functools import reduce

inicio = time.perf_counter()

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

def esTruncableDesdeDerecha(x):
    listaDigitos = obtenerListaDeDigitosDeNumero(x)
    tamaño = len(listaDigitos)    
    for i in range(0,tamaño-1):
        numero = obtenerNumeroDeLista(listaDigitos[0:tamaño-(i+1)])
        if numero not in primosSet:
            return False
    return True

def esTruncableDesdeIzquierda(x):
    listaDigitos = obtenerListaDeDigitosDeNumero(x)
    tamaño = len(listaDigitos)    
    for i in range(0,tamaño-1):
        numero = obtenerNumeroDeLista(listaDigitos[tamaño-(i+1):])
        if numero not in primosSet:
            return False
    return True


### Inicio Algoritmo

primos = criba(1000000)
primosSet = set(primos)
primosTruncables = []

for primo in primos[primos.index(7)+1:]:

    if esTruncableDesdeDerecha(primo) and esTruncableDesdeIzquierda(primo):
        primosTruncables.append(primo)

respuesta = reduce(lambda x, y: x+y,primosTruncables,0)

print(primosTruncables)
print(respuesta)

### Fin

fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
