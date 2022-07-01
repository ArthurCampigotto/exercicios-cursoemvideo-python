salario = float(input('Digite seu salário: '))
if(salario <= 1250):
    aumento = salario + (salario * 0.15)
    print('Seu novo salário com reajuste de 15% é de {:.2f} R$'.format(aumento))
else:
    aumento = salario + salario * 0.10
    print('Seu novo salário com reajuste de 10% é de {:.2f} R$'.format(aumento))