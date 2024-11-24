try:
    with open("/arquivo_restrito.txt", "r") as arquivo:
        conteudo = arquivo.read()
except IOError:  # Tratamento do erro IOError
    print("Erro: Problema ao acessar o arquivo!")
