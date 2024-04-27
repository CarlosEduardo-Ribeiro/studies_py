#Imprime a raiz utilizando a função "pow()"
from math import sqrt, floor
n = int(input('Digite um número:'))
r = pow(n, 1/2)
print('A raiz quadrada de {} é {}'.format(n, floor(r)))