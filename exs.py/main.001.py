#jogo de Jokenpô!
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Sua opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual a sua escolha? '))
if jogador != 1 and jogador != 2 and jogador != 3:
    print('\033[4;31mJOGADA INVÁLIDA, TENTE NOVAMENTE\033[m')
elif jogador == 1 or jogador == 2 or jogador == 3: 
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('=-='*9)
    print('Jogador jogou {}'.format(itens[jogador-1]))
    print('Computador jogou {}'.format(itens[computador]))
    print('=-='*9)
if computador == 0:
    if jogador-1 == 0:
        print('\033[1;7mEMPATE\033[m')
    elif jogador-1 == 1:
        print('\033[7;34;41mJOGADOR VENCE! :)\033[m')
    elif jogador-1 == 2:
        print('\033[1;34;41mCOMPUTADOR VENCE! :(\033[m')
elif computador == 1:
    if jogador-1 == 0:
         print('\033[1;34;41mCOMPUTADOR VENCE! :(\033[m')
    elif jogador-1 == 1:
        print('\033[1;7mEMPATE\033[m')
    elif jogador-1 == 2:
        print('\033[7;34;41mJOGADOR VENCE! :)\033[m')
else:
    if jogador-1 == 0:
        print('\033[7;34;41mJOGADOR VENCE! :)\033[m')
    elif jogador-1 == 1:
         print('\033[1;34;41mCOMPUTADOR VENCE! :(\033[m')
    elif jogador-1 == 2:
        print('\033[1;7mEMPATE\033[m')