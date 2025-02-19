# Operadores Lógicos

saldo = 1000
saque = 250
limite_saque = 150

# and -> Ambas as condições devem ser verdadeiras para retornar True
print(saque <= saldo and saque >= limite_saque)

# or -> Apenas um verdadeiro para retornar verdadeiro
print(limite_saque <= saldo or limite_saque >= saque)

# not -> Nega a condição. Verdadeiro vira falso, falso vira verdadeiro
print(not limite_saque <= saque)