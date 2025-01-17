from functools import reduce
from triangulo_pascal import triangulo_pascal
import sys

try:
    n = int(sys.argv[1])

    if n < 1:
        raise ValueError("Por favor, proporcione un número válido (≥1)")

    a = triangulo_pascal(n)
    res = reduce(lambda acc,x: acc + x**2,a )
    print(res)
except:
    print("Por favor, proporcione un número válido (≥1)")



