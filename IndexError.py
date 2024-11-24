try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:  # Tratamento do erro IndexError
    print("Erro: Índice fora dos limites da lista!")
