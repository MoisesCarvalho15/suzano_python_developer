# Estrutura de Repetição While

while True:
    print("[1] - Opção 1\n[2] - Opção 2\n[3] - Sair")
    entrada_usuario = input("Digite uma opção: ")
    
    if entrada_usuario == "1":
        print("Você escolheu a Opção 1\n")
    elif entrada_usuario == "2":
        print("Você escolheu a opção 2\n")
    elif entrada_usuario == "3":
        print("Saindo do programa")
        break # forçando a saída do programa
    else:
        print("Digite uma opção válida\n")