#Lê um nopme completo e imprime o primeiro e o ultimo nome
allname = str(input('Digite seu nome completo '))
name = allname.split()
print('prazer em te conhecer!')
print('seu primeiro nome é {}'.format(name[0]))
print('e o seu ultimo nome é {}'.format(name[len(name)-1]))