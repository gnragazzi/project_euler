from math import ceil

def esAñoBisiesto(año):
    if año % 4 != 0:
        return False
    else:
        if año %100 == 0 and año % 400 != 0:
            return False
        else:
            return True
def crearListaPrimerosDias(año):
    esBisiesto = esAñoBisiesto(año)
    cantidad_dias_por_mes = {
        "enero":31,
        "febrero": 29 if esBisiesto else 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31,
    }
    accum = 1
    dia_primero = []
    for _,v in cantidad_dias_por_mes.items():
        dia_primero.append(accum)
        accum += v
    return dia_primero

def primerDomingoAño(año):
    if(año < 1900):
        return -1
    pri_dom = 7

    for a in range(1900,año):
        esBisiesto=esAñoBisiesto(a)
        dif = 2 if esBisiesto else 1
        pri_dom = (((pri_dom - 1)-dif)%7) + 1

    return pri_dom

def crearListaDomingos(año):
    a = primerDomingoAño(año)
    return [x:=a+i*7 for i in range(0,ceil(365//7)+1) if a+i*7 <= 365]
    

def cuantosDomingosSonPrimeroDeMesEn(año):
    lista_domingos = crearListaDomingos(año)
    lista_primero_mes = crearListaPrimerosDias(año)
    #print(lista_domingos)
    #print(lista_primero_mes)
    tam_dom = len(lista_domingos)
    tam_pri = len(lista_primero_mes)
    i = 0
    j = 0
    cont = 0

    while(i < tam_dom and j < tam_pri):
        if(lista_domingos[i] == lista_primero_mes[j]):
            cont += 1
            i+=1
            j+=1
        elif (lista_domingos[i]  > lista_primero_mes[j]):
            j += 1
        else:
            i += 1

    return cont

def domingosPrimeroDeMesEnRango(añoInicio,añoFinal):
    cont = 0
    for año in range(añoInicio,añoFinal + 1):
        cont += cuantosDomingosSonPrimeroDeMesEn(año)
    return cont

print(domingosPrimeroDeMesEnRango(1901,2000))
