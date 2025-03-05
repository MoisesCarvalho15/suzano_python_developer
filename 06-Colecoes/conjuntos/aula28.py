# Criando sets

# Criando uma lista e um tupla com valores duplicados
numeros = [1, 2, 3, 1, 3, 4]
carros = ("palio", "gol", "celta", "palio")

print(numeros)
print(carros)

# Eliminando itens duplicados de uma lista
numeros2 = set(numeros)
carros2 = set(carros)

print(numeros2)
print(carros2)

# Acessando os sets
# Para acessar eles, devem ser transformados em listas
linguagens = {"python", "java", "python", "javascript"}

# print(linguagens[0]) # erro
linguagens = list(linguagens)
print(linguagens)
print(linguagens[0])
