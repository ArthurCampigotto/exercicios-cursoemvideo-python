total_gasto = 0
total_produto_1000 = 0
mais_barato = 0
cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto R$: '))
    total_gasto += valor
    cont += 1
    if valor > 1000:
        total_produto_1000 += 1
    if cont == 1 or valor < mais_barato:
        mais_barato = valor
        barato = nome     
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if resp == 'N':
        break
print('Fim do programa')
print(f'O total da compra é de R${total_gasto:.2f}')
print(f'{total_produto_1000} produtos custam mais de R$1000.00')
print(f'O produto mais barato  foi {barato} e custou R${mais_barato:.2F}')