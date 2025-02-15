from os import system
import sys
from importlib import reload

def clear():
    system("clear")
    reload(sys.modules[__name__])

def p27(n=1000):
    c = buscar_constante(n)
    return ((2*-1*c+1) * (c**2-c+41))

def buscar_constante(n=1000):
    c = 1    
    while True:
        c += 1
        res = c**2-c+41
        if abs(res) > 1000:
            break
    return c -1            
