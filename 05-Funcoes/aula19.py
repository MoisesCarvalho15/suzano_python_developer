# Parâmetros por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Os parâmetros que foi criado após a barra, podem ser mencionados na hora de chamar a função    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

# Se os parâmetros que estão antes da barra for mencionados, irá gerar um erro de positional only
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
