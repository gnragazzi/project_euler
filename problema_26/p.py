from importlib import reload
from os import system
from decimal import Decimal,getcontext
from math import floor,sqrt

getcontext().prec = 5000


def clear():
    system("clear")

def listar(n=1000, inicio=2):
    for i in range(inicio,n+1):
        print(f"1/{i}: {1/i}")

def listar_potencias_2(n):
    i = 1    
    denominador = 2**i
    while denominador <= n:
        cociente = 1/denominador
        print(f"1/{denominador}: {cociente}")
        i +=1
        denominador = 2**i

def dividir(n):
    print(Decimal(1)/Decimal(n))

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
    return [x for x in range(2,n) if(lista[x-1])]

def contar_longitud_ciclo(n):
    _, num = str(Decimal(1)/Decimal(n)).split(".")
    tam_ciclo = 1
    tam_str = len(num)    
    while(tam_ciclo < tam_str):
        i = 0
        esCiclo = True
        while(i + tam_ciclo < tam_str - 100):
            if(num[i] == num[i+tam_ciclo]):
                i +=1
                continue
            else:
                esCiclo = False
                break
        if(esCiclo):
            return tam_ciclo
        else:
            tam_ciclo += 1
    return -1
            

def maximo(d):
    a = criba_eratostones(d)
    longitudes = []
    for i in a:
        longitudes.append((i,contar_longitud_ciclo(i)))
    longitudes.sort(reverse= True, key=lambda t: t[1])
    return longitudes[0]
