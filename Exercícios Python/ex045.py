from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('-=-' * 10)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))   
print('-=-' * 10)
if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU !')
    elif jogador == 2:
        print('COMPUTADOR VENCEU !')
    else:
        print('Jogada Inválida')
elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU !')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU !')
    else:
        print('Jogada Inválida')

elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU !')
    elif jogador == 1:
        print('COMPUTADOR VENCEU !')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')    