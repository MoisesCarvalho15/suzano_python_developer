# Objetos de primeira classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado é = {resultado}")
   
exibir_resultado(5, 5, somar)
exibir_resultado(10, 5, subtrair)
