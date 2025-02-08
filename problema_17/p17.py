from functools import reduce

one = len("one")
two = len("two")
three = len("three")
four = len("four")
five = len("five")
six = len("six")
seven = len("seven")
eight = len("eight")
nine = len("nine")

unidad = [one,two, three, four, five, six, seven, eight, nine]

primera_decena = [len("ten"), len("eleven"), len("twelve"), len("thirteen"), len("fourteen"), len("fifteen"), len("sixteen"), len("seventeen"), len("eighteen"), len("nineteen")]
twenty = len("twenty")
thirty = len("thirty")
fourty = len("forty")
fifty = len("fifty")
sixty = len("sixty")
seventy = len("seventy")
eighty = len("eighty")
ninety = len("ninety")
hundred = len("hundred")
thousand = len("thousand")

otras_decenas = [twenty, thirty,fourty,fifty,sixty,seventy,eighty,ninety]

ocurrencias_unidad = 9*10+100 #9 ocurrencias en 0..99 por las 10 veces que encontramos ese intervalo (una por cada centena), más 100 ocurrencias en 100..199
ocurrencias_decena = 10 * 10 #hay 10 ocurrencias en 0..99 y este intervalo se repite 10 veces

res = one*(ocurrencias_unidad+1) + ocurrencias_unidad * (two + three + four + five + six + seven + eight + nine)
res += reduce(lambda acc, x: x+acc,primera_decena) * 10 #hay 10 ocurrencias de la primera decena
res += ocurrencias_decena * (twenty + thirty + fourty + fifty + sixty + seventy + eighty + ninety)
res += (hundred) * 900 + len("and") * 855 +  thousand

print(res)

def cantidad_letras(n):
    n_str = list(str(n))
    n_str.reverse()
    res = 0
    for i, u in enumerate(n_str):
        u = int(u)
        if(i == 0 and u > 0):
            res+= unidad[u-1]
        elif(i == 1 and u == 1):
            res = primera_decena[int(n_str[0])]
        elif(i == 1 and u != 0):
            res += otras_decenas[u-2]
        elif(i == 2):
            res += (unidad[u-1] + hundred)
            if(int(n_str[0])!= 0 or int(n_str[1])!=0):
                res += len("and")
        elif(i==3):
            res = one + thousand
        #print(i,u,res)
    return res

def p_17(limite):
    res = 0
    for i in range(1,limite + 1):
        suma = cantidad_letras(i)
        res += suma
        print(f"número: {i}, valor: {suma}, suma_parcial: {res}")
    return res

def prueba():
    for i in range(1,100):
        print(f'i: {i}, esperado: {cantidad_letras(i)+len("onehundredand")-cantidad_letras(i+100)}')

