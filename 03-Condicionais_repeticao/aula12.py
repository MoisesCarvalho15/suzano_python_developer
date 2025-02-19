# Estrutura Condicionais ternária

saldo = 2000
tentativa_saque_1 = 2500
tentativa_saque_2 = 1500

status_1 = "Sucesso" if tentativa_saque_1 <= saldo else "Falha"
status_2 = "Sucesso" if tentativa_saque_2 <= saldo else "Falha"

print(f"{status_1} ao realizar o saque.")
print(f"{status_2} ao realizar o saque.")
