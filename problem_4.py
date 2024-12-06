#

#construir el conjunto de todos los números que sean resultado del producto de dos números de m cifras

m = 3

a = [x*y for x in range(10**(m-1),10**(m)) for y in range(10**(m-1),10**(m))]
a.sort()


b = [x*y for x in range(10**(m-1),10**(m)) for y in range(10**(m-1),10**(m))]
palindr = -1

while(palindr < 0):
    num_str = str(a.pop())
    i = 0
    n = len(num_str) - 1
    cond = True
    while(i < (n - i) and cond):
        if(num_str[i] == num_str[n-i]):
            i += 1
        else:
            cond = False
            break
    if(cond):
        palindr = int(num_str)


            
