LIMITE_SAQUES = 3
limite = 500
saldo = 0
extrato = ""
numero_saques = 0

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

while True:
    opcao = input(menu)

    # Opção de Depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    # Opção de Extrato
    elif opcao == "3":
        print("\n--- EXTRATO ---")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("----------------")

    # Opção de Sair
    elif opcao == "4":
        print("Obrigado por usar nosso serviço. Até logo!")
        break

    # Opção inválida 
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
