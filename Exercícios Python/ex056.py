somaidade = 0
mediaidade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0
for p in range(1,5):
    print('------{}ª PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade < maior_idade_homem:
       maior_idade_homem = idade 
       nome_velho = nome
    if sexo in 'Ff' and idade > 20:
        tot_mulher_20 += 1
mediaidade = somaidade / 4
print('A media do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem,nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot_mulher_20)) 