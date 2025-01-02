#https://projecteuler.net/problem=10
from math import floor, sqrt
from aux_euler import esPrimo
from functools import reduce
import sys

#versión greedy
def suma_primos_hasta(n):
    lista_primos = [x for x in range(2,n+1) if(esPrimo(x))]
    return reduce(lambda a,b: a+b, lista_primos)    

#criba de Eratóstones:https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def criba_eratostones(n):
    lista = [True for i in range(1,n+1)]
    lista[0] = False
    primo = 2
    lim = floor(sqrt(n))
    while primo <= lim:
        multiplo = primo * primo
        while multiplo <= n:
            lista[multiplo-1] = False
            multiplo += primo
        for primo in range(primo+1,lim + 2):
            if lista[primo-1]:
                break
    sum = 0
    for i in range(0,len(lista)):
        if(lista[i]):
            sum += (i+1)
    return sum

if(len(sys.argv) < 2):
    print(f"Programa {sys.argv[0]}: Ingrese un número entero mayor que 1 como argumento.")
else:
    try:
        print(suma_primos_hasta(int(sys.argv[1])))
        print(f"Criba: {criba_eratostones(int(sys.argv[1]))}")
    except ValueError:
        print(f"ERROR: el argumento ingresado '{sys.argv[1]}' no es un número.\nPor Favor, ingrese un número mayor a 1")
        exit()



