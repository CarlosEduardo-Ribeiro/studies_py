# Sequência = - X^30/1 + X^29/4 - X^28/3 + X^27/16 ... S = soma
x = float(input('Digite um número: '))
expo = 30 
count = 0
soma = 0
S = []
print('S = ', end=(' '))
for i in range(30):
        if i %2 == 0:
                termo = -x**expo/1+count
                expo -= 1
                soma += termo 
                S.append(termo)
                print('a{} = - {:.0f}^{}/{}, '.format(i + 1, x, expo+1, 1+i), end=(''))
        elif i %2 != 0:
                expo-= 1
                i += 1
                termo = (x**expo)/(i**2)
                expo -= 1
                soma += termo
                count += 2
                S.append(termo)
                print('a{} = + {:.0f}^{}/{}, '.format(i, x, expo+2, i**2),end=(''))
print('\n')
print('soma = {:.0f}'.format(soma))