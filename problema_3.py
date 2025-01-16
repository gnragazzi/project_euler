#https://projecteuler.net/problem=3

def factor_primo_mas_grande(x):
	i = 2
	while(i < x):
		if(x%i==0):
			x = x//i
		else:
			i+=1
	return x

print(factor_primo_mas_grande(600851475143)) #6857
