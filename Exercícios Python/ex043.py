peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso/ (altura ** 2)
print(' O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >=40:
    print('Obesidade Mórbida')
