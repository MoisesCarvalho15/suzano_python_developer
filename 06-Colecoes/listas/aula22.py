# Acesso e fatiamento de listas

# índ negt -4        -3       -2      -1
# índice    0         1        2       3
frutas = ["Maçã", "Laranja", "Pera", "Uva"]

print(frutas[0])
print(frutas[3])
# índice negativo
print(frutas[-2])
# Índice 1 até o final da lista
print(frutas[1:])
# índice 0 até o índice 1
print(frutas[:2])
# Invertendo os dados da lista
print(frutas[::-1])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pegando do índice 1 até o 10 pulando de 2 em 2
print(numeros[1:11:2])
