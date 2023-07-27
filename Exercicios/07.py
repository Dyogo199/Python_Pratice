def eh_palindromo(palavra):
    palavra = palavra.lower().replace("","")
    return palavra == palavra[::-1]

palavra1 = "arara"
palavra2 = "python"
palavra3 = "ame a ema"

print(eh_palindromo(palavra1))
print(eh_palindromo(palavra2))
print(eh_palindromo(palavra3))
