TAMAÑO_DIRECCION = 4
# Leer el archivo con la matriz 
def parsea_matriz(nombre_archivo):
    lista = []
    f = open(nombre_archivo,'r')
    for linea in f:
        lista.append(linea.split())
    longitud = len(lista[0])
    for i in range(1,len(lista)):
        if longitud != len(lista[i]):
            return null
    for i in range(0,len(lista)):
        for j in range(0,longitud):
            lista[i][j] = int(lista[i][j])
    return lista

matriz =  parsea_matriz("./aux/ej_11_matriz.txt")

# recorrer la matriz en búsqueda del producto más alto

if(matriz):
    maximo = 0
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    for i in range(0,num_filas):
        for j in range(0,num_columnas):
            offset_x_positivo = j + TAMAÑO_DIRECCION <= num_columnas  
            offset_y = i + TAMAÑO_DIRECCION <= num_filas        

            if(offset_x_positivo):
                producto = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
                maximo = maximo if maximo > producto else producto
                if(offset_y):
                    producto = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
                    maximo = maximo if maximo > producto else producto
            if(offset_y): 
                producto = matriz[i][j] * matriz[i+1][j] * matriz[i+2][j] * matriz[i+3][j]
                maximo = maximo if maximo > producto else producto
                offset_x_negativo = j + 1 >= TAMAÑO_DIRECCION
                if(offset_x_negativo):
                    producto = matriz[i][j] * matriz[i+1][j-1] * matriz[i+2][j-2] * matriz[i+3][j-3]
                    maximo = maximo if maximo > producto else producto
    print(maximo)
