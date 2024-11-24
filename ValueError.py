try:
    numero = int("abc")
except ValueError:  # Tratamento do erro ValueError
    print("Erro: Não é possível converter 'abc' em um número inteiro!")
