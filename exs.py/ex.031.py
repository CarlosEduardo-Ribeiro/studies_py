#Retorna a idade e a necessidade de alistamento militar obrigatório ou não
from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
if idade>18:
    print('Você nasceu em {} e tem {} anos em {} \n'.format(nasc, idade, atual), end = ' ')
    print('Seu alistamento foi em {}'.format(nasc + 18))
elif idade == 18:
    print('Você term 18 anos e deve se alistar imediatamente!')
else:
    print('Você nasceu em {} e tem {} anos em {} seu alistamento será em {}'.format(nasc, idade, idade + 18))