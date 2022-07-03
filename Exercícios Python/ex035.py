n1 = float(input('Digite a primeira reta: '))
n2 = float(input('Digite a segunda reta: '))
n3 = float(input('Digite a terceira reta: '))

if(n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2):
    print('As retas acima PODEM formar um triangulo !')
else:
    print('As retas acima NÃO PODEM formar um triangulo')