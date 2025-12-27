valores_disponibles = [1,2,5,10,20,50,100,200]
pila = []

def euler31(x):
    for valor in valores_disponibles:
        if valor <= x:
            pila.append(valor)
        else:
            break
    return rec_coin(pila, x)    


def rec_coin(pila, valor):
    contador = 0
    while len(pila)>0:
        candidato = pila.pop()
        if(candidato == 1):
            return contador + 1
        resto = valor - candidato
        if(resto == 0):
            contador = contador + 1
        else:
            pila_aux = pila[:]
            if(resto >= candidato):
                pila_aux.append(candidato)
            contador = contador + rec_coin(pila_aux, resto)

def improvedEuler31(x):
    for valor in valores_disponibles:
        if valor <= x:
            pila.append(valor)
        else:
            break
    return improvedRecCoin(x, len(pila) - 1)

def improvedRecCoin(valor, indice):
    if indice <= 0:
        return 1
    contador = 0
    while valor >= 0:
        print(valor, pila[indice -1])
        contador = contador + improvedRecCoin(valor, indice - 1)
        valor = valor - pila[indice]
    return contador
