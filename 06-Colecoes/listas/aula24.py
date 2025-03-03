# Métodos de lista

lista_mercado = ["macarrão", "feijão"]

# Adicionando um item na lista de cada vez
lista_mercado.append("arroz")
# Adicionando mais de um item na lista
lista_mercado.extend(["mistura", "óleo", "produtos de limpeza"])
print(lista_mercado)

# Vendo o tamanho da lista
print(len(lista_mercado))

# Removendo o item pelo index
lista_mercado.pop() # último item
lista_mercado.pop(0) # primeiro item
print(lista_mercado)

# Removendo um item específico
lista_mercado.remove("óleo")
print(lista_mercado)

# Ordenando a lista em ordem ascendente
lista_mercado.sort()
print(lista_mercado)

# Ordenando a lista em ordem descendente
lista_mercado.reverse()
print(lista_mercado)

# retornando o index de um determinado item
print(lista_mercado.index("mistura"))

# Criando uma cópia de uma lista
lst_mercado2 = lista_mercado.copy()
print(lst_mercado2)

# verificando a quantidade do mesmo item na lista
print(lst_mercado2.count("arroz"))

# Limpando o conteúdo de uma lista
lst_mercado2.clear()
print(lst_mercado2)
