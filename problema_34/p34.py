from math import factorial
listaFactorial = [factorial(i) for i in range(10)]
respuesta = []

def obtenerListaDeDigitosDeNumero(x):
    lista = []
    while x > 0:
        lista.append(x % 10)
        x = x // 10
    lista.reverse()
    return lista

for i in range(3, 11199999):
    numeroComoLista = obtenerListaDeDigitosDeNumero(i)
    sumaFactoriales = 0
    for digito in numeroComoLista:
        sumaFactoriales = sumaFactoriales + listaFactorial[digito]
    if sumaFactoriales == i:
        print(i)
        respuesta.append(i)
    

