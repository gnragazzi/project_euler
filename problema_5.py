#https://projecteuler.net/problem=5

def minimoMultiplo(n):
	multiplicidades = []
	respuesta = 1
	for i in range(2,n+1):
		multiplicidades.insert(i-2,0)
		factor = 2
		numero = i
		multiplicidad = 0
		while factor <= numero:
			if numero % factor == 0:
				numero = numero / factor
				multiplicidad += 1
			else:
				if(multiplicidad > multiplicidades[factor-2]):
					multiplicidades[factor-2]=multiplicidad
				factor +=1
				multiplicidad = 0
		if(multiplicidad > multiplicidades[factor-2]):
			multiplicidades[factor-2]=multiplicidad
	print(multiplicidades)
	for i in range(n,1,-1):
		respuesta *= i ** multiplicidades[i-2]
	return respuesta


