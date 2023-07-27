def Calcular_Soma (lista):
    soma =  sum(lista)

    media = soma/len(lista)
    return soma

def Media(lista):
    media = (sum(lista)//len(lista))
    return media

lista = [0,1,2,3,4,5,6,7,8,9]

n = Calcular_Soma(lista)
m = float(Media(lista))

print(f"A soma é: {n}")
print(f"A media é: {m}")