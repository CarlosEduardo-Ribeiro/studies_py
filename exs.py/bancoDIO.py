movimentacao = []

def menu():
    print('''
    SISTEMA BANCÁRIO DIO

Digite a opção desejada:
[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Ver extrato
[ 4 ] Sair''')

def menu_saque():
    print('''Você escolheu [ 2 ] Sacar
Para sacar, deve-se seguir os seguintes critérios:
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
    return deposito

def realizar_saque(deposito):
    menu_saque()
    lim_saque = 0
    while lim_saque < 3:
        saque = float(input('\nQuanto gostaria de sacar? '))
        if saque > 500:
            print('Valor digitado maior que R$ 500.00, tente novamente.')
            continue
        if saque > deposito:
            print(f'Valor solicitado de R$ {saque:.2f} é maior que o saldo disponível de R$ {deposito:.2f}')
            break
        deposito -= saque
        movimentacao.append({"tipo": "Saque", "valor": saque})
        lim_saque += 1
        continua = input('Deseja sacar novamente? (s/n) ').strip().lower()
        if continua == 'n':
            break
    if lim_saque == 3:
        print('Você atingiu o limite de 3 saques diários.')
    return deposito

def main():
    deposito = 0.0
    while True:
        menu()
        try:
            escolha = int(input('Qual será o serviço solicitado? '))
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue
        
        if escolha == 1:
            deposito += realizar_deposito()
        elif escolha == 2:
            deposito = realizar_saque(deposito)
        elif escolha == 3:
            exibir_extrato()
        elif escolha == 4:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
