velocidade = float(input('digite a velocidade que passou pelo radar: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Você foi multado e o valor da multa será R${:.2f}'.format(multa))
else:
    print('Você não foi multado')