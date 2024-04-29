x = float(input('Digite um número: '))
expo = 30
S = []
soma = 0
count = 0
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
# -X**30/1+i + X**29/i**2 - X**27/1+i + X**26/i**2 - X**25/1+i + X**24/i**2 - X**23/1+i
# I = 0 A cada termo i+=1
