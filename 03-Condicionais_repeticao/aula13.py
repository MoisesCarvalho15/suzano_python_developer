# Estrutura de Repetição For

palavra = "Python"

# Iterando para cada caractere dentro da variável
for letra in palavra:
    # Imprimindo cada letra da palavra em maiúscula
    print(letra.upper())
    
print()

# Utilizando o for e o range
tabuada = int(input("Digite o número da tabuada: "))
                #start,      stop      , step
for numero in range(0, tabuada * 10 + 1, tabuada):
    print(numero, end=" ")
