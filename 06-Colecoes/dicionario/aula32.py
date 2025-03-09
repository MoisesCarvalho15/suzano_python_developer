contatos = {
    "moisés": {"idade": 24, "cnh": False, "telefone": '12345-6789'},
    "guilherme": {"idade": 28, "cnh": True, "telefone": '93333-3333'},
    "henrique": {"idade": 30, "cnh": True, "telefone": '94444-4444'}    
}

# Criando uma cópia do Dicionário
contatos_copy = contatos.copy()
print(list(contatos_copy.keys())) # Retornando as chaves em forma de lista

# Apagando o dicionário
contatos_copy.clear()
print(contatos_copy)

# Criando dicionário com os valores da chave none
dict_none = dict.fromkeys(["nome", "telefone"])
print(dict_none, end="\n\n")

# Criando um dicionário com um valor padrão
dict_padrao = dict.fromkeys(["nome", "telefone"], "vazio")
print(dict_padrao, end="\n\n")

# Acessando valores 
print(contatos.get("guilherme")) # Retorna chaves e valores
print(contatos.get("nome")) # Se não existir, retorna um none
print(contatos.get("cidade", {}), end="\n\n") # Se não existir, retorna um dicionário vazio

# Acessando as chaves
print(contatos.keys(), end="\n\n") # Retorna as chaves  do dicionário

# Acessando as chaves e os valores 
print(contatos.items(), end="\n\n")

# Removendo uma chave específica
contatos.pop("henrique")
print(contatos)
print(contatos.pop("henrique", {}), end="\n\n") # Se não existir, retorna uma chave vazia

# Removendo a última chave
print(contatos.keys()) # Exibindo somente as chaves
print(contatos.popitem()) # Removendo a última chave
print(contatos.keys(), end="\n\n")  # Exibindo somente as chaves

# Criando um novo dicionário
contato = {"nome": "Moisés", "idade": 24}
print(contato)

# Adicionando um valor caso ele não exista
#                     chave       valor
contato.setdefault("sobrenome", "Carvalho") # Se não existir a chave sobrenome, ele coloca o valor passado
print(contato)
contato.setdefault("nome", "Carlos") # Se a chave existir, ele deixa o valor padrão
print(contato, end="\n\n")

# Atualizando o dicionário com uma chave não existente
print(contatos.keys())
contatos.update({"Carlos": {"idade": 30, "cnh": False, "telefone": None}})
print(contatos.keys(), end="\n\n")

# Retornando todos os valores das chaves
print(contatos.values(), end="\n\n")

# Verificando se tem a chave
print("moisés" in contatos) # Retorna um valor Bool
print("joão" in contatos, end="\n\n")

# Verificando se tem uma determinada chave dentro da chave
resultado = "idade" in contatos["Carlos"] # Retorna um valor Bool
print(resultado, end="\n\n")

# Removendo um valor específico de uma chave
print(contatos["moisés"])
del contatos["moisés"]["idade"]
print(contatos["moisés"])
