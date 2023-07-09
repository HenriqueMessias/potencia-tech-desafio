import datetime
menu = '''
    [0]: Depositar
    [1]: Sacar
    [2]: Extrato
    [3]: Sair
'''

saldo = 0
saque_limite = 500
extrato = ''''''
saque_quantidade = 0
SAQUE_LIMITE_QTD = 3

while True:

    opcao = input(menu)

    match str(opcao):
        case '0': # Deposito
            deposito = float(input('Informe o valor do deposito a ser realizado: R$'))
            if deposito > 0:
                saldo+=deposito
                extrato+= f'Deposito realizado às {str(datetime.datetime.today()).split(".")[0]} no valor de: R${deposito:.2f}\n'
            else:
                print('Operacao falhou! Valor inserido é inválido.')
        case '1': # Saque
            saque = float(input('Informe o valor que deseja sacar: R$'))
            
            if saque > 0: # Valida se o valor inserido é positivo 
                if saque_quantidade < SAQUE_LIMITE_QTD:
                    if saque <= saque_limite:
                        if saque < saldo: # Valida se o saque é coerente com o saldo disponível
                            saldo-=saque
                            saque_quantidade+=1
                            extrato+= f'Saque realizado às {str(datetime.datetime.today()).split(".")[0]} no valor de: R${saque:.2f}\n'
                        else:
                           print('Operacao falhou! Você não possui saldo suficiente.')
                    else:
                        print(f'Operacao falhou! Valor inserido excede o limite para saque.\nValor limite para saque: R${saque_limite:.2f}')
                else:
                        print(f'Operacao falhou! Número máximo de saques excedido.\nLimite de saques: {SAQUE_LIMITE_QTD}')
            else:
                print('Operacao falhou! Valor inserido é inválido.')
                
        case '2':
            print('\n============================ EXTRATO ============================')
            print('Não foram realizadas movimentações. ' if not extrato else extrato)
            print(f'\nSaldo Total R${saldo:.2f}')
            print('=================================================================')
        case '3':
            print('Até breve')
            break
        case default:
            print('Opcao invalida, digite novamente uma das opcoes acima')
