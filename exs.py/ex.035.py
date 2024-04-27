s = 0
cont = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c 
print('o somatório de todos {} números ímpares múltiplos de três no intervalo de 1 a 500 é {}'.format(cont, s))