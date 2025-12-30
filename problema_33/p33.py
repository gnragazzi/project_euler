listaNumerosDisponibles = [[x,y] for x in range(1,10) for y in range(1,10)]
listaDeEjemplos = []

def listarDenominadores(x):
    return [listaNumerosDisponibles[i] for i in range(x+1,len(listaNumerosDisponibles)) if (listaNumerosDisponibles[i][0] == listaNumerosDisponibles[x][0] or listaNumerosDisponibles[i][0] == listaNumerosDisponibles[x][1] or listaNumerosDisponibles[i][1] == listaNumerosDisponibles[x][0] or listaNumerosDisponibles[i][1] == listaNumerosDisponibles[x][1])]

def obtenerFraccionSimplificada(x,y):
    fraccionSimplificada = (x,y)    
    for i in x:
        for j in y:
            if i==j:
                fraccionSimplificada[0].remove(i)
                fraccionSimplificada[1].remove(j)
                return (fraccionSimplificada[0][0],fraccionSimplificada[1][0])

def obtenerNumeroDeLista(x):
    res = 0
    for i in range(len(x)):
        res = res + x[i] * (10**(len(x)-1-i))
    return res
                
def esRespuesta(x,y):
    fraccionOriginal = (obtenerNumeroDeLista(x),obtenerNumeroDeLista(y))
    fraccionSimplificada = obtenerFraccionSimplificada(x[:],y[:])
    
    cocienteOriginal = fraccionOriginal[0] / fraccionOriginal[1]
    cocienteSimplificado = fraccionSimplificada[0] / fraccionSimplificada[1]        

    if cocienteOriginal == cocienteSimplificado:
        return True

    return False

def resolverProblema(x):
    productoNumerador = 1
    productoDenominador = 1    

    for numerador, denominador in x:
        productoNumerador = productoNumerador * obtenerNumeroDeLista(numerador)
        productoDenominador = productoDenominador * obtenerNumeroDeLista(denominador)

    return (productoNumerador, productoDenominador)
        

for indice, numerador in enumerate(listaNumerosDisponibles):
    listaDenominadores = listarDenominadores(indice)
    for denominador in listaDenominadores:
        if esRespuesta(numerador, denominador):
            listaDeEjemplos.append((numerador,denominador))
print(listaDeEjemplos)
print(resolverProblema(listaDeEjemplos))
