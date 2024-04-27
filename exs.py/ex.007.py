a = int(input('Digite um número:'))
if a<=10:
    if (a%2) == 0:
        print('O valor', a, 'é menor ou igual à 10 e é par')
    else:
        print('O valor', a, 'é menor ou igual à 10 e é ímpar')
else:
    print('O valor', a, 'é maior que 10')   