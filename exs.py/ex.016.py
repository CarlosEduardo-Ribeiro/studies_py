#Imprime a parte inteira de um float utilizando a fnção "trunc()"
from math import trunc
n = float(input('Digite um número:'))
print('A porção inteira de {} é {}'.format(n, trunc(n)))