Sb = float(input('Salário base:'))
I = float()
if Sb<= 2000.00:
    I = Sb*0.08
    Va = 500
    print('Imposto: {}\nvale alimentação: {}\nsalário a receber: {}'.format(I, Va, (Sb-I)))
elif 2000.01<=Sb<=5000.00:
    I = Sb*0.09
    Va = 400
    print('Imposto: {}\nvale alimentação: {}\nsalário a receber: {}'.format(I. Va, (Sb-I)))
else:
    I = Sb*0.11
    Va = 300
    print('Imposto: {}\nvale alimentação: {}\nslário a receber: {}'.format(I, Va, (Sb-I)))