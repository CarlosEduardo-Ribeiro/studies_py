#Imprime se um aluno foi aprovado, reprovado ou está de recuperação com base na entrada de dados das notas e faltas
nome = input('Nome do aluno:')
n1 = float(input('Digite a primeira nota do(a) {}:'.format(nome)))
n2 = float(input('Digite a segunda nota do(a) {}:'.format(nome)))
n3 = float(input('Digite a terceira nota do(a) {}:'.format(nome)))
media = float((n1*3+n2*4+n3*3)/10)
faltas = float(input('Digite o número de faltas do(a) {}:'.format(nome)))
if media >=6 and faltas<=20:
    print('O(a) aluno(a) {} foi aprovado(a) com a média igual à {}'.format(nome, media))
else:
    print('O(a) aluno(a) {} doi reprovado(a)'.format(nome))