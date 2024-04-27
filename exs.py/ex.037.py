
s = 0
cont = 0
for c in range (0, 6):
    n = int(input('{}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma de todos os {} números pares solicitados é {}'.format(cont, s))