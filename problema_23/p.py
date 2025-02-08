from math import floor, sqrt
from importlib import reload
from functools import reduce
from os import system

def clear():
    system("clear")

def divisores_propios_ordenados(n):
    divisores = {1}
    limite_superior = floor(sqrt(n))
    for i in range(2,limite_superior+1):
        if(n%i==0):
            divisores.add(i)
            divisores.add(n//i)
    divisores = list(divisores)
    divisores.sort()
    return divisores

def divisores_propios(n):
    divisores = {1}
    limite_superior = floor(sqrt(n))
    for i in range(2,limite_superior+1):
        if(n%i==0):
            divisores.add(i)
            divisores.add(n//i)
    return divisores

def suma_divisores_propios(n):
    div = divisores_propios(n)
    return reduce(lambda acc, x: acc + x, div)

def esAbundante(n):
    return True if suma_divisores_propios(n) > n else False

def imprimir_lista_divisores_propios_y_estatus(n):
    div = divisores_propios(n)
    for d in div:
        print(f"{d}: {esAbundante(d)}")

def lista_abundantes(lim_inf=1,lim_sup=28123,paso=1):
    l = []
    for i in range(lim_inf,lim_sup+1,paso):
        if esAbundante(i):
            l.append(i)
    return l

def comprobar_hipotesis2(x):
    '''si x es abundante, kx con k=1,2,...,(28123//k)+1 es abundante'''
    if(esAbundante(x)):
        a = [n:=x*k for k in range(1,(28123//x)+1)]
        for xk in a:
            if(not esAbundante(xk)):
                return (xk, False)
        return True
    else:
        return None

def p23(lim_inferior=12, lim_superior=28123):
    if lim_superior > 28123:
        lim_superior = 28123 #se sabe que todos los números superiores a este son sumas de números abundantes
    lista_num = [True for i in range(0,lim_superior + 1)]
    numeros_abundantes = {12}

    for i in range(lim_inferior,lim_superior + 1):
        if(lista_num[i] and esAbundante(i)):
            for k in range(1,(lim_superior//i)+1):           
                ik = i*k
                numeros_abundantes.add(ik)
                lista_num[ik] = False
    numeros_abundantes = list(numeros_abundantes) # tal vez sea innecesario

    lista_num = [True for i in range(0,lim_superior + 1)]

    for i in range(0,len(numeros_abundantes)):
        for j in range(i,len(numeros_abundantes)):
            total = numeros_abundantes[i]+numeros_abundantes[j]
            if(total > lim_superior):
                continue
            else:
                lista_num[total] = False

    res = 0
    for num,esValido in enumerate(lista_num):
        if(esValido):
            res += num

    return res

