
#solución por fuerza bruta
def terna_pitagorica(n):
    lista = [(a,b,c) for a in range(3,(n-3)//3) for b in range(a+1,(n-a)//2) for c in range(b+1,n-a-b+1) if(a+b+c==1000 and a**2+b**2==c**2)]
    num1, num2, num3 = lista[0]
    return num1 * num2 * num3


