#Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
print('\n----------> Bem vindo ao WHS.Bank <----------')
menu = '''
    Menu:
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair

=> '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if (opcao == "1"):
        valor = float(input('Informe o valor de depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "2":
        valor = float(input('Iforme o valor do saque: R$ '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! Você não tem limite suficiente.')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == "3":
        print("\n############# EXTRATO #############")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Número de saques permitidos {LIMITE_SAQUES - numero_saques}")
        print("\n###################################")

    elif opcao == "0":
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')