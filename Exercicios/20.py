def remover_duplicatas(lista_numeros):
    return list(set(lista_numeros))

# Exemplo de uso da função
numeros = [1, 2, 3, 2, 4, 1, 5]
numeros_unicos = remover_duplicatas(numeros)
print("Números únicos:", numeros_unicos)
