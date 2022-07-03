numero = int((input('Digite um número para saber sua tabuada: ')))
aux = 0
print('*'* 18)
print('Tabuada de {}'.format(numero))
print('*'* 18)

while (aux <= 10):
    print('{} X {} = {}'.format(aux,numero,(aux * numero)))
    aux += 1