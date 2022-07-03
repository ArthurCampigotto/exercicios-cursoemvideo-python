real = float(input('Quanto de dinheiro você tem na carteira ? '))
dolar = real / 5.19
euro = real / 5.45

print('Com R${} você pode comprar US${:.2f} e EU${:.2F}'.format(real,dolar,euro))