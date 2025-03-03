# Iterando os valores

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros)

# buscando somente os números pares da lista
for numero in numeros:
    if numero % 2 == 0:
        print(f"O número {numero} é PAR")

# List Comprehension
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
