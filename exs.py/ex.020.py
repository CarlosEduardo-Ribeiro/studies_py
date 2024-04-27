#Retorna "True" para toda cidade que tenha "santo" no nome
cid = str(input('cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')