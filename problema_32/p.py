digitosDecimales = [x for x in range(1,10)]
listaMultiplicandosDeDosDigitos = [[x,y] for x in digitosDecimales for y in digitosDecimales if x!=y]
listaProductosPandigitales = []
valorMaximo = 10000

    
def listarPosiblesMultiplicadoreDeMultiplicando(x):
    limiteSuperior = valorMaximo // obtenerNumeroDeLista(x)
    aux = digitosDecimales[:]
    for digito in x:
        aux.remove(digito)
    if len(x) == 1:
        return [[x,y,z,w] for x in aux for y in aux for z in aux for w in aux if x != y and x!=z and x!=w and y!=z and y!=w and z!=w and (x*1000 + y*100 + z* 10 + w) <= limiteSuperior ]
    elif  len(x) == 2:
        return [[x,y,z] for x in aux for y in aux for z in aux if x != y and x!=z and y!=z and (x*100 + y*10 + z) <= limiteSuperior]
    else:
       raise ValueError('Wrong Multiplicand number of digits')

def obtenerNumeroDeLista(x):
    res = 0
    for i in range(len(x)):
        res = res + x[i] * (10**(len(x)-1-i))
    return res

def obtenerListaDeDigitosDeNumero(x):
    lista = []
    while x > 0:
        lista.append(x % 10)
        x = x // 10
    lista.reverse()
    return lista

def esProductoPandigital(x,y,z):
    aux = digitosDecimales[:]
    for n in x:
        if n not in aux:
            return False
        aux.remove(n)
    for n in y:
        if n not in aux:
            return False
        aux.remove(n)
    for n in z:
        if n not in aux:
            return False
        aux.remove(n)
    return True

for multiplicando in digitosDecimales[1:]:
    posiblesMultiplicadores = listarPosiblesMultiplicadoreDeMultiplicando(obtenerListaDeDigitosDeNumero(multiplicando))
    for multiplicador in posiblesMultiplicadores:
        multiplicadorComoNumero = obtenerNumeroDeLista(multiplicador)
        producto = multiplicando * multiplicadorComoNumero
        if esProductoPandigital(obtenerListaDeDigitosDeNumero(multiplicando), multiplicador, obtenerListaDeDigitosDeNumero(producto), ) and producto not in listaProductosPandigitales:
            listaProductosPandigitales.append(producto)

for multiplicando in listaMultiplicandosDeDosDigitos:
    posiblesMultiplicadores = listarPosiblesMultiplicadoreDeMultiplicando(multiplicando)
    for multiplicador in posiblesMultiplicadores:
        multiplicandoComoNumero = obtenerNumeroDeLista(multiplicando)
        multiplicadorComoNumero = obtenerNumeroDeLista(multiplicador)
        producto = multiplicandoComoNumero * multiplicadorComoNumero
        if esProductoPandigital(multiplicando, multiplicador, obtenerListaDeDigitosDeNumero(producto), ) and producto not in listaProductosPandigitales:
            listaProductosPandigitales.append(producto)

respuesta = 0

for producto in listaProductosPandigitales:
    respuesta = respuesta + producto

print(listaProductosPandigitales)
print(respuesta)

