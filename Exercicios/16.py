def encontrar_maior_menor(lista_numeros):
    if not lista_numeros:
        return None, None
    maior = menor = lista_numeros[0]
    for num in lista_numeros:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    return maior, menor

# Exemplo de uso da função
numeros = [23, 45, 12, 67, 3, 98, 5]
maior_numero, menor_numero = encontrar_maior_menor(numeros)
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
