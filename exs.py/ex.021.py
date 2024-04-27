#Retorna "True" se a string conter a cadeia.upper() conter "SILVA"
nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))