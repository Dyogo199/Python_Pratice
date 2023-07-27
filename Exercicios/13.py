def inverter_lista (lista):
    return lista[::-1]


lista_original = [1,2,3,4,5,6]
lista_invertidade = inverter_lista(lista_original)
print("Lista original: ", lista_original)
print("Lista invertida: ", lista_invertidade)