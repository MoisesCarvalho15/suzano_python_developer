# Entrada de dados do usuário

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(f"O {nome} tem {idade} anos.")

# Trocando a quebra de linha
print("Na função print, o final da linha", end="... por padrão seria uma quebra de linha\n")
# Trocando o separador padrão
print(nome,idade, sep="_")