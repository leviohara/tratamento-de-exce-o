try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:  # Tratamento do erro FileNotFoundError
    print("Erro: Arquivo não encontrado!")
