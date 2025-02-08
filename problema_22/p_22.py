def parser(filename):
    try:
        f = open(filename,"r")
    except:
        print("Error abriendo el archivo. Saliendo...")
        quit()
    str_input = f.readline().strip()
    str_input = str_input.split(",")
    f.close()
    str_input =  list(map(lambda x: x.strip("\""),str_input))
    str_input.sort()
    return str_input
    


def p22(filename):
    lista_nombres = parser(filename)
    total = 0
    for indice, nombre in enumerate(lista_nombres):
        parcial = 0
        for letra in nombre:
            parcial += ord(letra)-64
        total += parcial * (indice + 1)

    return total

a = p22("names.txt")
