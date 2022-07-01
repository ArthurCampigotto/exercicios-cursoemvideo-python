from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(0,7):
    nasc = int(input('Digite em que ano a {}ª pessoa nasceu: ').format(pessoa))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas de maior'.format(totmaior))
print('E também tivemos {} pessoas de menor'.format(totmenor))