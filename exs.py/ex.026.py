#Imprime se uma variável n é par ou ímpar
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))