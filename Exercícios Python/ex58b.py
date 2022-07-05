import random
numero_aleatorio = random.randint(0,5)
tentativas = 0
acertou = False
print('-'*50)
print('Vou pensar um número de 0 a 10, tente adivinhar')
print('-'*50)
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    tentativas += 1
    if jogador == numero_aleatorio:
        acertou = True
    else:
        if jogador < numero_aleatorio:
            print('Mais... Tente mais uma vez.')
        elif jogador > numero_aleatorio:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(tentativas))
