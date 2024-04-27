#Imprime todos os números pares ou ímpares em um intevalo de 0 até o valor de entada n de tipo int 
n = int(input('Digite um número: '))
for c in range(0, n+1, 2):
    print(c)
print('FIM')