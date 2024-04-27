#Modifica uma string e imprime ela em .upper() .lower(), imprime o comprimento da cadeia e do "primeiro nome"
name = str(input('Digite seu nome completo:')).strip()
print('upper: {}'.format(name.upper()))
print('lower: {}'.format(name.lower()))
print('len all: {}'.format(len(name) - name.count(' ')))
print('len first name: {}'.format(name.find(' ')))