def CuentaDigitosFibo(n):
    prev = 1
    curr = 0
    longitud = 0
    i = 0
    while longitud < n:
        next = curr + prev
        prev = curr
        curr = next
        longitud = len(str(curr)) 
        i += 1
    return i
