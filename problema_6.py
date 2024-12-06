#https://projecteuler.net/problem=6

def diferencia_suma_cuadrados_por_fuerza_bruta(n):
	x = 0
	y = 0
	for i in range (1,n+1):
		x += i**2
		y += i
	y *= y
	return y - x

#planteando la resta como resta de sumatorias, reemplazando las sumatorias por sus equivalentes, expandiendo y simplificando llegamos a la siguiente fórmula. Si tomamos como medida la cantidad de operaciones, la función por fuerza bruta es O(n) mientras que la otra es O(1)

def diferencia_suma_cuadrados_eficiente(n):
	return (3*(n**4)+2*(n**3)-3*(n**2)-2*n)//12
