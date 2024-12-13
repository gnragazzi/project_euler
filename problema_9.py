import sys

suma = 0
try:
	suma = int(sys.argv[1])
except:
	print("Ejecute este programa con un número como argumento")
	quit()

#solución fuerza bruta
def prod_terna_pitagorica(n):
    lista = [(a,b,c) for a in range(3,(n-3)//3) for b in range(a+1,(n-a)//2) for c in range(b+1,n-a-b+1) if(a+b+c==1000 and a**2+b**2==c**2)]
    num1, num2, num3 = lista[0]
    return num1 * num2 * num3

#solución en base a las observaciones del ejercicio 
def prod_terna_pitagorica_param(s):
	for m in range(2,s//2+1):
		aux = s//2
		# Lo primero es encontrar un m tal que m | s/2
		if aux % m != 0:
			continue
		k = m + 1
		aux = s//(2*m)
		# También debemos encontrar un k=(m-n) tal que m<k<m/2 y k | s/2*m
		while(k < 2*m):
			if(k%2==0):#por definición, k es impar
				k += 1
				continue
			if(aux % k == 0):
				break
			k += 1
		if(k>= 2*m):
			continue # si no hay tal k, debemos probar con otro m
		aux = m
		mcd = 2
		#por último, debemos saber si MCD(m,k)=1
		while mcd < aux:
			if(aux%mcd==0):
				if(k%mcd==0):
					break
				aux = aux // mcd
			mcd += 1
		#si no hay MCD, entonces tenemos nuestro m y k
		if(mcd>=aux):
			n = k-m
			d = s//(2*m*k)
			a = (m**2 - n**2)*d
			b = (2*m*n)*d
			c = (m**2 + n**2)*d
			return a*b*c
	return -1

print(prod_terna_pitagorica_param(suma))
