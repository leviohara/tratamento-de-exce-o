try:
    numero = 10
    numero.append(5)
except AttributeError:  # Tratamento do erro AttributeError
    print("Erro: O objeto 'int' não possui o método 'append'!")
