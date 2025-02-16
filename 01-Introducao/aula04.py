# Convertendo tipos de dados

numero_1 = 10
numero_2 = 50.5

# Imprimindo os tipos das variáveis
print(f"{numero_1} = {type(numero_1)}")
print(f"{numero_2} = {type(numero_2)}\n")

# Convertendo float para int
numero_2 = int(numero_2)
print(f"{numero_2} = {type(numero_2)}")

# Convertendo int para float
numero_1 = float(numero_1)
print(f"{numero_1} = {type(numero_1)}\n")

# Declarando novas variáveis
idade = "29"
peso = "68.3"
print(f"{idade} = {type(idade)}")
print(f"{peso} = {type(peso)}\n")

# Convertendo uma string para int ou float
idade = int(idade)
peso = float(peso)
print(f"{idade} = {type(idade)}")
print(f"{peso} = {type(peso)}")