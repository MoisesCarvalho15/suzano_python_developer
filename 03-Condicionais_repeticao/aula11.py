# Estrutura Condicionais if aninhado

conta_normal = False
conta_universitaria = False
conta_especial = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saque <= saldo:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:
    if saque <= saldo:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

elif conta_especial:
    print("Conta especial realizada")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")
