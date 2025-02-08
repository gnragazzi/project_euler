from sys import argv

limite_superior = int(argv[1])

a = [-1 for i in range(0,(limite_superior*9+4))]

maximo = 0
respuesta = 0

a[0] = 1
#ahorro = 0
for i in range(1,limite_superior + 1):
    cont = 1
    n = i
    camino = []
    while(n != 1):
        if( n <= len(a) and a[n-1] >= 0):
            #ahorro += a[n-1]-cont
            cont += a[n-1] - 1
            break
        camino.append(n)
        n = n//2 if n%2==0 else n*3+1
        cont +=1
    for idx, num in enumerate(camino):
        if(num<=len(a)):
            a[num-1] = cont - idx
    if(cont > maximo):
        maximo = cont
        respuesta = i

#print(f"se ahorraron {ahorro} iteraciones")
print(respuesta, maximo)
