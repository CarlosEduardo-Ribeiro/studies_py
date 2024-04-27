#Imprime a tabuada de um número porém utilizando o laço for
n = int(input('Digite um número: '))
print('--------------')
for c in range (1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('--------------')