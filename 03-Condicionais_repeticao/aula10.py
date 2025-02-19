# Estrutura Condicionais if, elif, else

idade = 18
dinheiro_cnh = False

if idade >= 18 and dinheiro_cnh == True:
    print("Você está apto para começar as aulas para ter sua CNH.")
elif idade >= 18 and dinheiro_cnh == False:
    print("Você ainda precisar ter o dinheiro para começar as aulas.")
elif idade < 18 and dinheiro_cnh == True:
    print("Você precisa ter 18 anos para começar as aulas.")
else:
    print("Você precisa ter no mínimo 18 anos e ter o valor total para começar a fazer as aulas.")
