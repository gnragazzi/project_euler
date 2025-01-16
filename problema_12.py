from math import floor,sqrt
'''n_triangular = 0
for i in range(1,200):
    n_triangular += i
    factores = []
    for j in range(1, n_triangular + 1):
        if(n_triangular % j == 0):
            factores.append(j)
    print(f"{i}° - {n_triangular}: {factores}")

'''

def factores(n):
    factores = []
    for i in range(1,n+1):
        if(n%i==0):
            factores.append(i)
    return factores

def ef_factores(n):
    factores = {1,n}
    limite_superior = floor(sqrt(n))
    for i in range(1,limite_superior+1):
        if(n%i==0):
            factores.add(i)
            factores.add(n//i)
    return factores

def cantidad_factores(x):
    if(n%2!=0):
        print(f"n: {len(factores(n))} // n/2: {len(factores(int((n+1)/2)))}")
    else:
        print(f"n/2: {len(factores(int(n/2)))} // n: {len(factores(n+1))}")

def num_triangular_con_x_divisores(x):
    if(x <= 0):
        return None
    n = 0
    factores_n = 0
    m = 1
    factores_m = 1
    n_es_par = True
    while(factores_n * factores_m < x):
        n += 1
        m += 1
        n_es_par = not n_es_par
        factores_n = factores_m
        if(n_es_par):
            factores_m = len(ef_factores(m))
        else:
            factores_m = len(ef_factores(m//2))
    return (n*m) // 2
