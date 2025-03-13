menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def exibir_mensagem(titulo, mensagem):
    print(f"\n================ {titulo} ================")
    print(mensagem)
    print("==========================================")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            exibir_mensagem("DEPÓSITO", f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            exibir_mensagem("ERRO", "Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            exibir_mensagem("ERRO", "Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            exibir_mensagem("ERRO", "Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            exibir_mensagem("ERRO", "Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            exibir_mensagem("SAQUE", f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            exibir_mensagem("ERRO", "Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        exibir_mensagem("EXTRATO", "Não foram realizadas movimentações." if not extrato else extrato + f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        exibir_mensagem("ERRO", "Operação inválida, por favor selecione novamente a operação desejada.")