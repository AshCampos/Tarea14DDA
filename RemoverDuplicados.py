#Programa que elimina los elementos duplicados en un arreglo y regresa el numero de elemento y el arreglo con los elementoa unicos
def removerDuplicados(a):
 
    if len(a) == 0:
        return 0
    
    numsUnicos = 0

    for i in range(1, len(a)):
        if a[i] != a[numsUnicos]:
            numsUnicos += 1
            a[numsUnicos] = a[i]
    
    k = numsUnicos + 1
    return k

arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 9, 9, 9]
k = removerDuplicados(arr)
print("Longitud del arreglo con elementos unicos:", k)
print("Arreglo con elementos únicos:", arr[:k])
