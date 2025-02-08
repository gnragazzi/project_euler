from sys import argv

limite_superior = int(argv[1])

maximo = 0
respuesta = 0

for i in range(1,limite_superior + 1):
    cont = 1
    n = i
    while(n != 1):
        n = n//2 if n%2==0 else n*3+1
        cont +=1
    if(cont > maximo):
        maximo = cont
        respuesta = i
        
print(respuesta, maximo)
