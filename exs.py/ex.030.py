#Calculo do valor de um financiamento
salario = float(input('Salário do comprador: R$ '))
valor_da_casa = float(input('valor da casa: R$'))
anos = int(input('Quantos anos o comprador ira pagar? '))
prestacao = valor_da_casa/(anos*12)
if prestacao < salario/3.33:
    print('O valor da prestação será R${:.2f}'.format(prestacao))
else:
    print('Emprestimo negado')