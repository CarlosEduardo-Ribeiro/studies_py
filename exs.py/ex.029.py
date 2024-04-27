#Imprime o maior valor entre três valores de entrada de tipo float
A = float(input('n1: '))
B = float(input('n2: '))
C = float(input('n3: '))
if A>B and A>C:
    print('O maior valor entre eles é o {}'.format(A))
elif B>A and B>C:
    print('O maior valor entre eles é o {}'.format(B))
elif C>A and C>B:
    print('O maior valor entre eles é o {}'.format(C))
elif A==B and A>C:
    print('Há dois valores iguais e é o {}'.format(A))
else:
    print('Todos os valores são iguais')