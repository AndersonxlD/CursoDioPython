import datetime as dt

menu = """1-Saque
2-Saldo
3-Deposito
4-Extrato
5-Sair
"""

saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    data_hoje = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    opcao = int(input(f"{menu}Digite uma das opções acima: "))

    if opcao == 1:
        valor_sacar = int(input("Digite o valor que deseja sacar: "))

        if numero_de_saques > LIMITE_SAQUES:
            print("---------------------")
            print("Numeros de saques do dia foi excedido!")
            pass
            print("---------------------")
        elif saldo >= valor_sacar:
            saldo -= valor_sacar
            numero_de_saques += 1
            print("---------------------")
            print("Saque realizado!")
            print("---------------------")
            extrato.append(f"{data_hoje} - Valor retirado: {valor_sacar}")
        else:
            print("---------------------")
            print("Saldo insuficiente!")
            print("---------------------")
            pass

    elif opcao == 2:
        print("---------------------")
        print(f"Seu saldo é: {saldo}")
        print("---------------------")
        pass

    elif opcao == 3:
        valor_depositar = int(input("Digite o valor que deseja depositar: "))
        if valor_depositar > 0:
            saldo += valor_depositar
            print("---------------------")
            print(f"Valor {valor_depositar} depositado!")
            extrato.append(f"{data_hoje} - Valor depositado: {valor_depositar}")
            print("---------------------")
        else:
            print("---------------------")
            print("Valor invalido!")
            print("---------------------")
            pass

    elif opcao == 4:
        print("---------------------")
        for i in extrato:
            print(i)
        print("---------------------")

    elif opcao == 5:
        break

    else:
        print("---------------------")
        print("Opcao invalida!")
        print("---------------------")
        pass


