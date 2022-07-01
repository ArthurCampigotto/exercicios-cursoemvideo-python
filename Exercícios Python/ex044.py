print('{:=^40}'.format(' LOJAS GUANABARAS '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] A Vista dinheiro/cheque
[2] A Vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 0.10)
elif opcao == 2:
    total = preço - (preço * 0.05)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de {:.2f}R$ SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 0.20)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcela))
else:
    total = preço 
    print('OPÇÃO INVALIDA de pagamento, tente novamente !')
print('Sua compra de R${:.2f} no final vai custar R${:.2f} no final.'.format(preço,total))