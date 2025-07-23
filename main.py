menu = """

Bem-vindo ao Banco Python!
Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falha. O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falha. Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falha. O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falha. Número máximo de saques atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falha. O valor informado é inválido.")

    elif opcao == "e":
        print("=== Extrato ===")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")