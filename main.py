import os
import random

# A conta possui respectivamente: Número, nome do cliente, telefone, email, saldo inicial, limite de crédito e senha.
dados_conta = [0,'','','','','','']
conta_bloqueada = False
# Histórico de operações (depósitos e saques)
historico_operacoes = []

# Limpa o terminal no windows ou no linux
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Verifica se o email contém "@" e pelo menos um "."
def validar_email(email):
    if email and "@" in email and "." in email.split("@")[1]:
        return True
    else:
        print('ERRO: O FORMATO DE EMAIL É INVÁLIDO.')
        return False
    
# Verifica se a senha tem pelo menos 6 caracteres e contém caracteres alfanuméricos
def validar_senha(senha, confirmacao):
    if senha and len(senha) >= 6 and any(char.isalnum() for char in senha):
        if senha == confirmacao:
            return True
        else:
            print('ERRO: AS SENHAS NÃO CONFEREM.')
            return False
    else:
        print('ERRO: A SENHA DEVE TER PELO MENOS 6 CARACTERES E CONTER CARACTERES ALFANUMÉRICOS.')
        return False

# Cadastra uma conta nova
def cadastrar_conta():
    print('BANK DK – CADASTRO DE CONTA\n')

    # Número da conta gerado automaticamente
    numero_conta = random.randint(1000,9999)
    dados_conta[0] = numero_conta
    print(f'NÚMERO DA CONTA: {numero_conta}')

    # Nome do cliente, não pode ser vazio
    nome_conta = ''
    while nome_conta == '':
        nome_conta = input('NOME DO CLIENTE: ')
        if nome_conta == '':
            print('ERRO: O NOME DO CLIENTE NÃO PODE ESTAR VAZIO.')
    dados_conta[1] = nome_conta

    # Número de telefone do cliente, não pode ser vazio
    telefone_conta = ''
    while telefone_conta == '':
        telefone_conta = input('TELEFONE.......:')
        if telefone_conta == '':
            print('ERRO: O TELEFONE NÃO PODE ESTAR VAZIO.')
    dados_conta[2] = telefone_conta

    # Email do cliente, validado na função validar_email()
    email_conta = ''
    while email_conta == '' or not validar_email(email_conta):        
        email_conta = input('EMAIL..........: ')
        if email_conta == '':
            print('ERRO: O EMAIL NÃO PODE ESTAR VAZIO.')
    dados_conta[3] = email_conta
   

    # Saldo inicial do cliente, deve ser maior ou igual a R$ 1000
    saldo_conta = -1
    while saldo_conta < 1000:
        saldo_conta_input = input('SALDO INICIAL...: ')
        if not saldo_conta_input:
            print('ERRO: O SALDO INICIAL NÃO PODE ESTAR VAZIO.')
        else:
            saldo_conta = float(saldo_conta_input)
            if saldo_conta < 1000:
                print('ERRO: O SALDO INICIAL DEVE SER MAIOR OU IGUAL A R$1000.')
    dados_conta[4] = saldo_conta

    # Limite de crédito da conta, deve ser maior que zero 
    limite_credito_conta = -1
    while limite_credito_conta < 0:
        limite_credito_conta_input = input('LIMITE DE CRÉDITO: ')

        if not limite_credito_conta_input:
            print('ERRO: O LIMITE DE CRÉDITO NÃO PODE ESTAR VAZIO.')
        else:
            limite_credito_conta = float(limite_credito_conta_input)
            if limite_credito_conta < 0:
                print('ERRO: O LIMITE DE CRÉDITO DEVE SER MAIOR OU IGUAL A 0.')
    dados_conta[5] = limite_credito_conta

    # Senha da conta, validada na função validar_senha()
    senha_conta = ''
    confirmacao_conta = ''
    senha_conta = input('SENHA............: ')
    confirmacao_conta = input('REPITA A SENHA...: ')
    while not validar_senha(senha_conta, confirmacao_conta):
        senha_conta = input('SENHA............: ')
        confirmacao_conta = input('REPITA A SENHA...: ')
        if senha_conta == '':
            print('ERRO: A SENHA NÃO PODE ESTAR VAZIA.')
    dados_conta[6] = senha_conta

    input('CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# Realiza depósitos na conta
def depositar_conta():
    print('BANK DK – SAQUE DA CONTA')

    # Verifica o número da conta
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    if numero_conta != dados_conta[0]:
        print('ERRO: NÚMERO DA CONTA INCORRETO.')
        return conta_bloqueada

    print(f'NOME DO CLIENTE: {dados_conta[1]}')

    # Valor do depósito, deve ser maior que zero
    valor_deposito = -1
    while valor_deposito <= 0:
        valor_deposito = float(input('VALOR DO DEPÓSITO: R$ '))
        if valor_deposito <= 0:
            print('ERRO: O VALOR DO DEPÓSITO DEVE SER MAIOR QUE ZERO.')
    
    # Armazena a operação no saldo e no histórico
    dados_conta[4] += valor_deposito 
    historico_operacoes.append(valor_deposito) 

    print('DEPÓSITO REALIZADO COM SUCESSO!')
    input('PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# Realiza saques na conta
def sacar_conta(conta_bloqueada):
    print('BANK DK – DEPÓSITO EM CONTA')

    # Verifica o número da conta
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    if numero_conta != dados_conta[0]:
        print('ERRO: NÚMERO DA CONTA INCORRETO.')
        return conta_bloqueada

    print(f'NOME DO CLIENTE: {dados_conta[1]}')

    # Verifica a senha da conta, se o usuário errar a senha 3 vezes a conta é bloqueada
    for _ in range(3): 
        senha = input('INFORME A SENHA: ')
        if senha == dados_conta[6]:
            break
        print('ERRO: SENHA INCORRETA.')
    else: 
        print('ERRO: SENHA INCORRETA. OPÇÕES 3, 4 E 5 DO MENU BLOQUEADAS.')
        return True

    # Valor do saque, deve ser maior que zero
    valor_saque = -1
    while valor_saque <= 0:
        valor_saque = float(input('VALOR DO SAQUE: R$ '))
        if valor_saque <= 0:
            print('ERRO: O VALOR DO SAQUE DEVE SER MAIOR QUE ZERO.')

    # Subtrai o saldo do usuário, se o valor do saque for maior que o saldo disponível
    # o banco usa o crédito do cliente se possível.
    if valor_saque <= dados_conta[4]:
        dados_conta[4] -= valor_saque
    elif valor_saque <= dados_conta[4] + dados_conta[5]:  
        dados_conta[5] -= valor_saque - dados_conta[4]
        dados_conta[4] = 0
        print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
    else:
        print('ERRO: SALDO E LIMITE DE CRÉDITO INSUFICIENTES.')
        return conta_bloqueada

    # A operação é armazenada no histórico de operações
    historico_operacoes.append(-valor_saque) 

    print('SAQUE REALIZADO COM SUCESSO!')
    input('PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# Realiza a consulta do saldo do cliente
def consultar_saldo(conta_bloqueada):
    print('BANK DK – CONSULTA SALDO')

    # Verifica o número da conta
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    if numero_conta != dados_conta[0]:
        print('ERRO: NÚMERO DA CONTA INCORRETO.')
        return conta_bloqueada

    print(f'NOME DO CLIENTE: {dados_conta[1]}')

    # Verifica a senha da conta, se o usuário errar a senha 3 vezes a conta é bloqueada
    for _ in range(3):  
        senha = input('INFORME A SENHA: ')
        if senha == dados_conta[6]:
            break
        print('ERRO: SENHA INCORRETA.')
    else:  
        print('ERRO: SENHA INCORRETA. OPÇÕES 3, 4 E 5 DO MENU BLOQUEADAS.')
        return True

    # Mostra o saldo e o limite de crédito para o usuário
    print(f'SALDO EM CONTA: R$ {dados_conta[4]}')
    print(f'LIMITE DE CRÉDITO: R$ {dados_conta[5]}')

    input('PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# Realiza consulta do extrato das operações 
def consultar_extrato(conta_bloqueada):
    print('BANK DK – EXTRATO DA CONTA')

    # Verifica o número da conta
    numero_conta = int(input('INFORME O NÚMERO DA CONTA: '))
    if numero_conta != dados_conta[0]:
        print('ERRO: NÚMERO DA CONTA INCORRETO.')
        return conta_bloqueada

    print(f'NOME DO CLIENTE: {dados_conta[1]}')

    # Verifica a senha da conta, se o usuário errar a senha 3 vezes a conta é bloqueada
    for _ in range(3):  
        senha = input('INFORME A SENHA: ')
        if senha == dados_conta[6]:
            break
        print('ERRO: SENHA INCORRETA.')
    else:  
        print('ERRO: SENHA INCORRETA. OPÇÕES 3, 4 E 5 DO MENU BLOQUEADAS.')
        return True

    print(f'LIMITE DE CRÉDITO: R$ {dados_conta[5]}')

    # Mostra as operações realizadas para o usuário.
    print('ÚLTIMAS OPERAÇÕES:')
    for valor in historico_operacoes:
        if valor < 0:
            operacao = 'SAQUE'
        else:
            operacao = 'DEPÓSITO'
        # Mostra as operações em valores absolutos
        print(f'{operacao}: R$ {abs(valor)}')

    # Mostra o saldo para o usuário e o alerta se o saldo for negativo.
    print(f'SALDO EM CONTA: R$ {dados_conta[4]}')
    if dados_conta[4] < 0:
        print('Atenção ao seu saldo!')

    input('PRESSIONE UMA TECLA PARA VOLTAR AO MENU...')

# Loop do menu principal
opcao = '0'
# Automaticamente sai do menu se a opção for '6'
while opcao != '6':

    # Opções do menu principal
    print('''\nBANK DK – ESCOLHA UMA OPÇÃO
(1) CADASTRAR CONTA CORRENTE
(2) DEPOSITAR
(3) SACAR
(4) CONSULTAR SALDO
(5) CONSULTAR EXTRATO
(6) FINALIZAR
          
    ''')

    opcao = input("SUA OPÇÃO: ")
    limpar()

    if opcao == '1':
        cadastrar_conta()

    if opcao == '2':
        depositar_conta()
    
    # As funções das opções 3, 4 e 5 não serão executadas se a conta estiver bloqueada 
    if opcao == '3':
        if conta_bloqueada:
            print('ERRO: A CONTA ESTÁ BLOQUEADA. OPÇÃO INDISPONÍVEL.')
            continue
            
        conta_bloqueada = sacar_conta(conta_bloqueada)

    if opcao == '4':
        if conta_bloqueada:
            print('ERRO: A CONTA ESTÁ BLOQUEADA. OPÇÃO INDISPONÍVEL.')
            continue
        conta_bloqueada = consultar_saldo(conta_bloqueada)

    if opcao == '5':
        if conta_bloqueada:
            print('ERRO: A CONTA ESTÁ BLOQUEADA. OPÇÃO INDISPONÍVEL.')
            continue
        conta_bloqueada = consultar_extrato(conta_bloqueada)
    
    if opcao == '6':
        # fazer novidade
        pass

limpar()
print()
