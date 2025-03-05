# Fatiamento de tuplas

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[0:3:2])
print(tupla[::-1])

# Iterando as tuplas
for letra in tupla:
    print(letra)

for indice, letra in enumerate(tupla):
    print(f"{indice}: {letra}")
