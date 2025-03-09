# Criando um dicionário

pessoa = {"nome": "Moisés", "idade": 24}
# utilizando um construtor
pessoa = dict(nome="Moisés", idade=24)

# add mais chave e valor
pessoa["cnh"] = False
pessoa["telefone"] = '12345-6790'

# consultando os valores de um dicionário
print(pessoa["nome"])
print(pessoa["idade"])

# reatribuindo os valores
pessoa["nome"] = "Guilherme"
pessoa["idade"] = 28
print(pessoa)
 