import datetime

def operacao_deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo+=valor_deposito
        extrato+= f'    Deposito realizado às {str(datetime.datetime.today()).split(".")[0]} no valor de: R${valor_deposito:.2f}\n'
        print(f'    ====== Deposito no valor de R${valor_deposito} realizado com sucesso! ======')
    else:
        print('    -!-!-! Operacao falhou! Valor inserido é inválido. -!-!-!')

    return saldo, extrato


def operacao_saque(*, saldo: float, valor_saque: float, extrato: str, saque_limite: float, qtd_saques: int, limite_saques: int):
    if valor_saque > 0: # Valida se o valor inserido é positivo 
        if qtd_saques < limite_saques:
            if valor_saque <= saque_limite:
                if valor_saque < saldo: # Valida se o saque é coerente com o saldo disponível
                    saldo-=valor_saque
                    qtd_saques+=1
                    extrato+= f'    Saque realizado às {str(datetime.datetime.today()).split(".")[0]} no valor de: R${valor_saque:.2f}\n'
                    print(f'    ====== Saque no valor de R${valor_saque} realizado com sucesso! ======')
                else:
                    print('    -!-!-! Operacao falhou! Você não possui saldo suficiente. -!-!-!')
            else:
                print(f'    -!-!-! Operacao falhou! Valor inserido excede o limite para saque. -!-!-!\n    -!-!-! Valor limite para saque: R${saque_limite:.2f} -!-!-!')
        else:
            print(f'    -!-!-! Operacao falhou! Número máximo de saques excedido. -!-!-!\n    -!-!-! Limite de saques: {limite_saques}                                -!-!-!')
    else:
        print('    -!-!-! Operacao falhou! Valor inserido é inválido. -!-!-!')

    return saldo, extrato, qtd_saques


def comando_exibir_extrato(saldo: float, *, extrato: str):
    print('\n    ============================== EXTRATO ===========================')
    print('    Não foram realizadas movimentações. ' if not extrato else extrato)
    print(f'\n    Saldo Total R${saldo:.2f}')
    print('    ==================================================================')


def ferramenta_buscar_usuario(cpf: str, lista_usuarios: list):
    return [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf]


def comando_criar_usuario(lista_usuarios: list):
    cpf_usuario = input('    $ Informe seu cpf para cadastrar (somente números): ')

    if len(ferramenta_buscar_usuario(cpf_usuario, lista_usuarios)) > 0:
        print('    -!-!-! Já existe um usuário cadastrado com esse cpf -!-!-!')
        return
    
    nome_usuario = input('    $ Informe seu nome completo: ')
    data_nascimento_usuario = input('    $ Informe sua data de nascimento (dd/mm/yyyy): ')
    endereco_usuario = input('    $ Informe seu endereço (rua, nro - bairro - Cidade/UF): ')

    lista_usuarios.append({'cpf': cpf_usuario, 'nome': nome_usuario, 'data_nascimento': data_nascimento_usuario, 'endereco': endereco_usuario})
    
    print(f'    ====== Usuário portador do cpf {cpf_usuario} cadastrado com sucesso! ======')


def comando_criar_conta(agencia: str, numero_conta: int, lista_usuarios: list):
    cpf_usuario = input('    $ Informe seu cpf para cadastrar (somente números): ')

    usuario = ferramenta_buscar_usuario(cpf_usuario, lista_usuarios)
    if len(usuario) > 0:
        print(f'    ====== Conta de número {numero_conta} e agencia {agencia} criada com sucesso! ======')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario[0], 'data_criacao': str(datetime.datetime.today()).split(".")[0]}
    
    print('\n    -!-!-! Usuário não encontrado, comando de criação de conta falhou! -!-!-!')


def comando_exibir_contas(lista_contas: list):
    print('\n    ======================== CONTAS CADASTRADAS ======================')
    print('    Não há contas cadastradas. ' if len(lista_contas) == 0 else '')
    for conta in lista_contas:
        print(f'''
            Agência: {conta['agencia']}
            Conta corrente: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            Criada em: {conta['data_criacao']}
            ''')


def core():

    menu = '''
    ============================== MENU ==============================
    Digite uma das opções abaixo e depois pressione ENTER:
    [0]: Depositar
    [1]: Sacar
    [2]: Extrato
    [3]: Novo Usuário
    [4]: Nova Conta
    [5]: Listar Contas 
    [6]: Sair
    '''

    saldo = 0
    saque_limite = 500
    extrato = ''''''
    saque_quantidade = 0
    SAQUE_LIMITE_QTD = 3
    AGENCIA = '1998'
    lista_usuarios = []
    lista_contas = []

    while True:

        opcao = input(menu+'\n    $  Opção selecionada: ')

        match str(opcao):
            case '0': # Deposito
                deposito = float(input('    $  Informe o valor do deposito a ser realizado: R$'))

                saldo, extrato = operacao_deposito(saldo, deposito, extrato)
            case '1': # Saque
                saque = float(input('    $  Informe o valor que deseja sacar: R$'))

                saldo, extrato, saque_quantidade = operacao_saque(saldo=saldo, valor_saque=saque, extrato=extrato, saque_limite=saque_limite, qtd_saques=saque_quantidade, limite_saques=SAQUE_LIMITE_QTD)

            case '2': # Extrato
                comando_exibir_extrato(saldo, extrato=extrato)
            case '3': # Criar Usuário
                comando_criar_usuario(lista_usuarios)
            case '4':
                numero_conta = len(lista_contas) + 1
                conta = comando_criar_conta(AGENCIA, numero_conta, lista_usuarios)
                if conta:
                    lista_contas.append(conta)
            case '5': # Listar Contas
                comando_exibir_contas(lista_contas)
            case '6':
                print('\n    Até breve')
                break
            case default:
                print('\n    Opcao invalida, digite novamente uma das opcoes acima')


if __name__ == '__main__':
    core()