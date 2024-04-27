#Conversão de metros(m) para km, hm. dam, etc...
M = float(input('Digite uma distância em metros:'))
print('A medida {:.3f} corresponde à:'.format(M), end=('\n'))
print('{:.3f}km\n{:.2f}hm\n{:.1f}dam'.format((M/1000), (M/100), (M/10), end=(' ')))
print('{}dm\n{}cm\n{}mm\n'.format((M*10), (M*100), (M*1000)))