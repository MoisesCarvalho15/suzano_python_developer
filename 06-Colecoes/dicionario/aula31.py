# Dicionário Aninhado
contatos = {
    "moisés": {"idade": 24, "cnh": False, "telefone": '12345-6789'},
    "guilherme": {"idade": 28, "cnh": True, "telefone": '93333-3333'},
    "henrique": {"idade": 30, "cnh": True, "telefone": '94444-4444'}    
}

# Consultando um dicionário aninhado
print(contatos["guilherme"]["idade"])
print(contatos["henrique"]["telefone"], '\n')

# Iterar sobre dicionário
for chave, valor in contatos.items():
    print(chave, valor)
