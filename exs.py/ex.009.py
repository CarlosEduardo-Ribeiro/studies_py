#Recebe dois valores inteiros e imprime sua soma, multiplicação e a divisão deles com o método ".format()"
A = int(input('Digite um valor:'))
B = int(input('Digite outro valor:'))
print('A soma de {} e {} é igual à {} \nE o produto é igual à {}. '.format(A, B, A+B, A*B), end=' ')
print('Já a divisão dos dois valores resulta em {:.2f}'.format(A/B))