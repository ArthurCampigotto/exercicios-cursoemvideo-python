n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} sua média é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('Aprovado !')
elif media < 5:
    print('Reprovado')
elif media >= 5:
    print('Recuperação')
