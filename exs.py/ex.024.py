#Jogo de advinhação
import random
escolha = int(input('escolha um número de 0 à 5: '))
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
if num == escolha:
    print('Ganhou!')
else:
    print('Perdeu! A resposta correta era {}'.format(num))