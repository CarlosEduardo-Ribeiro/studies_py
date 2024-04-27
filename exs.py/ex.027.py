#Imprime a preço de uma viagem com base na distância
distancia = float(input('Diga a kilometragem da viagem: '))
if distancia <= 200:
    print('O preço da viagem será R${}'.format(distancia*0.5))
else:
    print('O preço da viagem será R${}'.format(distancia*0.45))