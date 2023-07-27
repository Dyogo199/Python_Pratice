def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

# Exemplo de uso da função
limite = 100
resultado = fibonacci(limite)
print("Sequência de Fibonacci até", limite, ":", resultado)
