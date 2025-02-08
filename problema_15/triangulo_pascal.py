def triangulo_pascal(n):
    a = [1]
    while len(a)<=n:
        a.append(1)
        for i in range(len(a)-2,0,-1):
            a[i] += a[i-1]
    return a    
