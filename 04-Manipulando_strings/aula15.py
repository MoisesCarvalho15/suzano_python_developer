# Trabalhando com Strings

texto = "Aprendendo Python"

# texto todo em maiúsculo
print(texto.upper())

# texto todo em minúsculo
print(texto.lower())

# texto com a primeira letra de cada palavra em maiúsculo
print(texto.title(), end="\n\n")

curso = "     Python      "
print(curso + ".")

# remove todos os espaços em branco da string
print(curso.strip() + ".")

# remove somente os espaços em branco da esquerda
print(curso.lstrip() + ".")

# remove somente os espaços em branco da direita
print(curso.rstrip() + ".")
