nome = str(input('Digite se nome completo: ')).lower().strip()
print('A letra a Aparece {} vezes'.format(nome.count('a', 0,)))
print('O primeiro a aparace na posição {}'.format(nome.find('a') + 1))
print('O ultimo a aparace na posição {}'.format(nome.rfind('a') + 1))
