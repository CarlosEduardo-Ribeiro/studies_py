movimentacao = []
saldo = []
from time import sleep
def menu():
    sleep(1.5)
    print('''
    SISTEMA BANCÁRIO DIO

Digite a opção desejada:
[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Ver extrato
[ 4 ] Ver saldo 
[ 5 ] Sair''')

def menu_saque():
    print('''\nVocê escolheu [ 2 ] Sacar
Para sacar, deve-se seguir os seguintes critérios:\n
1 - Deve haver saldo disponível em sua conta bancária.
2 - O saque não deve ser maior que R$ 500.00.
3 - Você tem o limite de 3 saques diários.
\nCaso não siga os critérios acima, o sistema automaticamente o alertará.\n''')

def exibir_extrato():
    print('\nVocê escolheu [ 3 ] Ver extrato')
    print('Extrato:')
    if not movimentacao:
        print("Nenhuma movimentação realizada.")
    else:
        for item in movimentacao:
            print(f"{item['tipo']}: R$ {item['valor']:.2f}")
    print('')

def realizar_deposito():
    deposito = float(input('Quanto gostaria de depositar? '))
    while deposito <= 0:
        deposito = float(input('O depósito deve ser maior que zero. Quanto gostaria de depositar? '))
    movimentacao.append({"tipo": "Depósito", "valor": deposito})
    saldo.append(deposito)
    return deposito

def realizar_saque(deposito):
    menu_saque()
    lim_saque = 0
    while lim_saque < 3:
        saque = float(input('\nQuanto gostaria de sacar? '))
    
        if saque > deposito:
            print(f'Valor solicitado de R$ {saque:.2f} é maior que o saldo disponível de R$ {deposito:.2f}')
            break
        elif saque > 500:
            print('Valor digitado maior que R$ 500.00, tente novamente.')
            continue
        deposito -= saque
        movimentacao.append({"tipo": "Saque", "valor": saque})
        lim_saque += 1
        continua = input('Deseja sacar novamente? (s/n) ').strip().lower()
        if continua == 'n':
            break
    if lim_saque == 3:
        print('Você atingiu o limite de 3 saques diários.')
    return deposito
def exibir_saldo():
    print(f'Saldo: R$ {sum(saldo)}')
    
def main():
    deposito = 0.0
    while True:
        menu()
        try:
            escolha = int(input('Qual será o serviço solicitado? '))
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue
        match escolha: 
            case 1:
                deposito += realizar_deposito()
            case 2:
                deposito = realizar_saque(deposito)
            case 3:
                exibir_extrato()
            case 4:
                exibir_saldo()
            case 5:
                print("Saindo do sistema em...")
                for i in range(3):
                    sleep(1)
                    print(f'{3-i}')
                print('Até logo!')
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
