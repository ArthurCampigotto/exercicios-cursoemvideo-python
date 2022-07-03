valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é seu salário? '))
anos_pagar = float(input('Quantos anos irá pagar a casa? '))

prestacao_mensal = valor_casa / ( anos_pagar * 12)

if(prestacao_mensal > salario * 0.30):
    print('O empréstimo sera negado ! ')
else:
    print('Seu empréstimo foi aprovado !')
