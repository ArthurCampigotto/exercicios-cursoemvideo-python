distancia = float(input('Qual é a distancia da sua viagem? Km: '))
if(distancia <= 200):
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem que você irá pagar é de {:.2f} R$'.format(preco))