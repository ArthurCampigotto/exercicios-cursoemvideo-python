listanum = []
while True:
    listanum.append(int(input('Digite um número: ')))
    
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':
        break

    print('Valor adicionado com sucesso !')
    print('Quer continuar ? [S/N]')
    
