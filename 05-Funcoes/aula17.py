# Função sem parâmetro
def exibir_mensagem():
    print("Olá mundo!")

# Função com parâmetro obrigatório
def exibir_mensagem_2(nome):
    print(f"Olá {nome}, seja bem vindo!")

# Função com um parâmetro default
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Olá {nome}, seja bem vindo!")

# Chamando as funções
exibir_mensagem()
exibir_mensagem_2("Moisés")
exibir_mensagem_3() # Se não passar o valor, irá ser utilizado o valor default
exibir_mensagem_3("Guilherme")
