def retorno_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    print("Numero pares", pares)
    return pares

numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par = retorno_pares(numeros)
print(numeros)
print(par)
