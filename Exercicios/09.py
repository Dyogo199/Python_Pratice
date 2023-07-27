def Calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * Calcular_fatorial(numero -1)


print("Calcular Fatorial!!")
n = float (input("Digite o numero"))
resultado = Calcular_fatorial(n)
print(f"O fatorial de {n} é {resultado}. ")

