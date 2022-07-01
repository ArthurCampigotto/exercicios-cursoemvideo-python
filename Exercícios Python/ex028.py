import random
numero_aleatorio = random.randint(0,5)
print('-'*50)
print('Vou pensar um número de 0 a 5, tente adivinhar')
print('-'*50)
chute = int(input('Em que número eu pensei?: '))
if chute == numero_aleatorio:
    print('Você ganhou')
else:
    print('Você perdeu, o número aleatório é {}'.format(numero_aleatorio))