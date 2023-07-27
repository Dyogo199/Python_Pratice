def encontrar_nome_mais_longo(lista_nome):
    nome_mais_longo =  ""
    for nome in lista_nome:
        if len(nome) > len(nome_mais_longo):
            nome_mais_longo = nome
    return nome_mais_longo

nomes = ["Ana", "João", "Carolina", "Pedro", "Maria"]
mais_longo = encontrar_nome_mais_longo(nomes)
print(f"O nome mais longo é: {mais_longo}")