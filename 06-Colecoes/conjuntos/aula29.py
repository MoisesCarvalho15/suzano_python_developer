# Iterando sets
carros = {"gol", "celta", "palio", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos do set
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Unindo elementos
print(conjunto_a.union(conjunto_b))

# Intersecção do conjunto (onde os dados são iguais)
print(conjunto_a.intersection(conjunto_b))

# Diferença entre os conjuntos
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# Diferença simétrica
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

# Retorna se um conjunto é o subconjunto do outro
print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))

# Retorna se todos os elementos de conjunto está no outro
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

print(conjunto_d)
# Adicionando um elemento ao conjunto
conjunto_d.add(35)
conjunto_d.add(2) # se for um número repetido, ele será ignorado
print(conjunto_d)

# Copiando e Limpando um conjunto
conjunto_e = conjunto_d.copy()
print(conjunto_e)
conjunto_e.clear()
print(conjunto_e)

# Descantando um valor específico
conjunto_d.discard(1)
conjunto_d.discard(55) # se o valor não existir, ele é ignorado
print(conjunto_d)

# Retirando sempre o índice 0 de cada conjunto
conjunto_d.pop()
print(conjunto_d)

# Removendo um valor específico
conjunto_d.remove(35)
print(conjunto_d)

# Retornando se um elemento está dentro do conjunto
print(4 in conjunto_d)
print(10 in conjunto_d)

# Verificando o tamanho de um set
print(len(conjunto_d))