somaidade = 0
mediaidade = 0
maioridadeM = 0
nomevelho = ''
totalf20 = 0
for p in range(1,5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeM:
        maioridadeM = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalf20+=1
mediaidade = somaidade/4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maioridadeM, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalf20))