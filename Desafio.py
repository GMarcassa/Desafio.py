menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou! O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe a quantia do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= limite_de_saques

        if excedeu_saldo:
            print ("Operação falhou! Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print ("Operação falhou! O valor de saque excediu o limite.")

        elif excedeu_saques:
            print ("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou! Valor informado e inválido.")

    elif opcao == "e":
        print ("\n=========== EXTRATO ===========")
        print ("não foram realizados movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("================================")

    elif opcao == "q":
        break 

    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada.")

