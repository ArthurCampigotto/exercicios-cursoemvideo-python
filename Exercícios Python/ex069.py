tot18 = 0
total_homens = 0
total_mulher_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().split()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulher_20 += 1    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é {tot18}')
print(f'Ao todos temos {total_homens} homens cadastrados')
print(f'E temos {total_mulher_20} mulheres com menos de 20 anos')
