from sys import argv

limite_superior = int(argv[1])

a = [-1 for i in range(0,limite_superior)]

maximo = 0
respuesta = 0

for i in range(1,limite_superior + 1):
    cont = 0
    n = i
    while(n != 1):
        if(n<limite_superior and a[n-1] >= 0):
            cont += a[n-1]
            break
        n = n//2 if n%2==0 else n*3+1
        cont +=1
    a[i-1] = cont
    if(cont > maximo):
        maximo = cont
        respuesta = i

print(respuesta, maximo)
