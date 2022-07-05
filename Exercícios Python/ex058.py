import random
numero_aleatorio = random.randint(0,5)
tentativas = 0
print('-'*50)
print('Vou pensar um número de 0 a 10, tente adivinhar')
print('-'*50)
chute = int(input('Em que número eu pensei?: '))
while chute != numero_aleatorio:
    if chute > numero_aleatorio:
        print('Seu chute foi maior que o número aleatório')
    elif chute < numero_aleatorio:
        print('Seu chute foi menor que o número aleatório')
    chute = int(input('Chute novamente: '))    
    tentativas += 1
print('''Você acertou !
Você precisou de {} tentativas'''.format(tentativas))
