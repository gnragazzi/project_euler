from importlib import reload
from os import system
from functools import reduce
import sys

cuartas_potencias = [x ** 4 for x in range(0,10)]

def clear():
    system("clear")
    reload(sys.modules[__name__])

def suma_4tas_potencias(n):
    numero = str(n)
    suma = 0
    for digito in numero:
        suma += cuartas_potencias[int(digito)]
    return suma

def suma_5tas_potencias(n):
    numero = str(n)
    suma = 0
    for digito in numero:
        suma += quintas_potencias[int(digito)]
    return suma

def imp(n):
    print(f"{n}\tsuma={suma_5tas_potencias(n)}")

def fuerza_bruta(n):
    lista = []
    for i in range(10,n):
        suma = suma_5tas_potencias(i)
        if i == suma:
            lista.append(suma)
            #imp(i)
    return reduce(lambda x,acc: x+acc, lista)
    

def fuerza_bruta_mejorado(n):
    lista = []
    for i in range(10,n):
        numero = list(str(i))
        numero.sort(reverse=True)
        suma = 0
        for digito in numero:
            suma += quintas_potencias[int(digito)]
            if(suma > i):
                break
        if i == suma:
            lista.append(suma)
    if not len(lista) > 0:
        return -1
    return reduce(lambda x,acc: x+acc, lista)

