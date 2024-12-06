#https://projecteuler.net/problem=7

def esPrimo(x):
	divisor = 2
	limite_superior= x//divisor
	while divisor <= limite_superior:
		if(x % divisor == 0):
			return False
		else:
			divisor += 1
			limite_superior= x//divisor
	return True

def n_avo_primo(n):
	x = 1
	i = 0
	while(i < n):
		x += 1
		if(esPrimo(x)):
			i += 1
	return x


#n_avo_primo(10001)->104743
