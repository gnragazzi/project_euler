#https://projecteuler.net/problem=2

def prob_2():
	fibo = []
	fibo.append(1)
	fibo.append(2)
	i = 1
	proximo = fibo[i] + fibo[i-1]
	while(proximo<4000000):
		fibo.append(proximo)
		i += 1
		proximo = fibo[i] + fibo[i-1]
	return sum([x for x in fibo if x %2 == 0])
