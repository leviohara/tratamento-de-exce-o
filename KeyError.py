try:
    dicionario = {"a": 1, "b": 2}
    print(dicionario["c"])
except KeyError:  # Tratamento do erro KeyError
    print("Erro: A chave 'c' não existe no dicionário!")
