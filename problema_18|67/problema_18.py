import sys

def sum(n):
    return int ( n * (n+1) / 2 )

try:
    nombre_archivo = sys.argv[1]
    f = open(nombre_archivo,"r")
except:
    print("Ingrese un nombre de archivo válido")
    quit()

lista_entrada = []
nivel = 0

for linea in f:
    linea = linea.strip().split(" ")
    nivel += 1
    for num in linea:
        try:
            lista_entrada.append(int(num))
        except:
            print("error")
            quit()

lista_sumas_parciales = [0 for i in range(0,len(lista_entrada))]

lista_sumas_parciales[0] = lista_entrada[0]

lista_sumas_parciales.append(lista_entrada[0])

lim_sup = 1
lim_inf = 0

for i in range(1,nivel):
    indice_linea_anterior = lim_inf
    lim_inf = lim_sup
    lim_sup = sum(i+1)
    for j in range(lim_inf, lim_sup):
        if (j == lim_inf or j == lim_sup - 1):
            lista_sumas_parciales[j] = lista_sumas_parciales[indice_linea_anterior] + lista_entrada[j]
        else:
            p_i = lista_sumas_parciales[indice_linea_anterior]
            indice_linea_anterior += 1
            p_d = lista_sumas_parciales[indice_linea_anterior]
            lista_sumas_parciales[j] = p_i + lista_entrada[j] if p_i > p_d else p_d + lista_entrada[j]

ultima_linea = lista_sumas_parciales[lim_inf:lim_sup]

maxima_suma = ultima_linea[0]

for i in range(1,len(ultima_linea)):
    maxima_suma = ultima_linea[i] if ultima_linea[i] > maxima_suma else maxima_suma

print(maxima_suma)        

f.close()
