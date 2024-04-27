#Imprime um item aleatório de uma lista 
import random
a1 = str(input('Aluno 1:'))
a2 = str(input('Aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)
print('O aluno escolhido foi {}'.format(escolha))