#Assim como o ex 007 porém com o método ".format()"
A = int(input('Digite um valor:'))
if (A%2) == 0 and (A<=10):
  print('O valor {:.2f} é menor ou igual à 10 e é par'.format(A))
elif (A%2) == 0 and (A>10):
  print('O valor {:.2f} é maior que 10 e é par'.format(A))
elif (A%2) != 0 and (A<=10):
  print('O valor {:.2f} é menor ou igual à 10 e é ímpar'.format(A))
else:
  print('O valor {:.2f} é maior que 10 e é ímpar'.format(A))