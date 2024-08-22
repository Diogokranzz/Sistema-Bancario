class Conta:
    def __init__(self, numero_conta, saldo, nome=None):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.nome = nome

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositado R$ {valor:.2f}. Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Sacado R$ {valor:.2f}. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome, saldo_inicial):
        numero_conta = self.gerar_numero_conta()
        conta = Conta(numero_conta, saldo_inicial, nome)
        self.contas[numero_conta] = conta
        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")

    def gerar_numero_conta(self):
        # Implementar lógica para gerar números de conta únicos
        # (por exemplo, usando números aleatórios ou um contador)
        return 1234567890  # Placeholder

    def encontrar_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def depositar_em(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar_de(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

# Exemplo de uso
meu_banco = Banco()
meu_banco.criar_conta("João Silva", 1000)

while True:
    print("\nEscolha uma opção:")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar saldo")
    print("5. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome do titular da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        meu_banco.criar_conta(nome, saldo_inicial)
    elif opcao == '2':
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor do depósito: "))
        meu_banco.depositar_em(numero_conta, valor)
    elif opcao == '3':
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor do saque: "))
        meu_banco.sacar_de(numero_conta, valor)
    elif opcao == '4':
        numero_conta = int(input("Digite o número da conta: "))
        conta = meu_banco.encontrar_conta(numero_conta)
        if conta:
            conta.consultar_saldo()
        else:
            print("Conta não encontrada.")
    elif opcao == '5':
        break
    else:
        print("Opção inválida.")