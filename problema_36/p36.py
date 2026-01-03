# El problema se presenta, a priori, como una búsqueda de palíndromos en alguna de las dos bases, y el chequeo de si 
# su equivalente en la otra base es también palíndromo.
# Del análisis surge que la cantidad de palíndromos en un alfabeto de k símbolos en palabras de longitud n es exponencial; y se observa que la cantidad de palíndromos en ambas bases no varía significativamente, pues donde la base del exponente es más grande, se compensa con la mayor cantidad de dígitos que se necesitan para representar el número, resultando en cadenas más largas y, por lo tanto, en más combinaciones.
    # Se observa, sin embargo, que debe ser (marginalmente) mas eficiente pasar de binario a decimal
    # (multiplicación) que viceversa (división).
# Es también inmediato que en lugar de buscar en todos los números, aquellos que sean palíndromos, es más eficiente generar palíndromos y chequearlos

# La primera versión del algoritmo que resuelve el problema es, entonces
# 1. Generar una lista con palíndromos entre 1 y 1.000.000 en base 2 (deberían ser más de 1534 y menos de 2046)
    # a. La representación de estos palíndromos debería, probablemente, ser una lista de símbolos así, 101 sería [1,0,1], aunque también podría ser [True,False,True]
# 2. Para cada palíndromo de la lista:
    # Convertirlo a su equivalente en base 10
    # Si el equivalente es palíndromo también, entonces
        # Agregarlo a una lista de resultados
# 3. Sumar el valor de todos los elementos de la lista de resultados.

#######################

# En una re-versión de la solución, me encuentro con que hay lugar para mejoras si al generar los palíndromos binarios puedo asignar los valores decimales correspondientes. 
# Esta idea surge de una alternativa para generar palíndromos binarios:
    # Dado cualquier número binario b de longitud n, se tiene que:
        # b ++ b^R es un palíndromo binario (donde ++ es la operación de concatenación y b^R es el reverso de b)
        # b ++ 0 ++ b ^R es un palíndromo binario
        # b ++ 1 ++ b ^R es un palíndromo binario
    # y, si x es es valor decimal del número representado por b, se tiene que, respectivamente
        # x * 2^n + x = x*(2^n + 1)
        # x * 2^(n+1) + x = x*(2^(n+1) + 1) 
        # x * 2^(n+1) + 2^n + x = x*(2^(n+1) + 1) + 2^n
# De esta forma, aprobecho mi conocimiento del número a partir del cual se genera el próximo palíndromo binario para determinar el valor de este último.
# Esta idea, implementada con una cola, permite una solución iterativa, hasta que el valor calculado de un palíndromo binario sea mayor que el límite dispuesto. 
# Se hipotetiza el siguiente, como un algoritmo que genera la lista de todos aquellos palíndromos binarios, emparejados al valor decimal correspondiente:

# 1. Generar un arreglo con los valores de las potencias de 2. Se hipotetiza que esto dará una mejora marginal de tiempo al tener indexados estos cálculos repetitivos
# 2. Crear 1 cola y una lista: 
    # la cola tendrá el primer palíndromo binario y será el punto de partida al resto de los cálculos. Será representado como una tupla (listaDeSímbolosBinarios, valorDecimal). La primer tupla será: ([1], 1)
    # la lista contendrá la respuesta (en esta primera versión, todos los palindromos binarios cuyo valor sea menor al objetivo)
# 3. Se toma el primer objeto de la cola y se asigna a una variable auxiliar
# 4. Hasta que el valor decimal de la primer tupla sea superior al objetivo, hacer: 
    # 1. En base a la tupla en la variable auxiliar, calcular los 3 palíndromos binarios y el valor decimal asociado, siguiendo el orden y las instrucciones dispuestas anteriormente. 
    # 2. Para cada uno de estas nuevas tuplas, verificar si el valor es mayor al objetivo,
        # en caso de serlo, salir del loop
        # en caso de no serlo, agregar la tupla a la cola
    # 3. Agregar la tupla en la variable auxiliar a la lista de respuesta.

