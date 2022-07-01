from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo M ou F.'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos no ano {}'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa de alistar imediatamente !')
elif idade > 18:
    saldo = idade - 18
    print('Seu tempo alistamento éra a {} anos atrás'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para você se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

    
