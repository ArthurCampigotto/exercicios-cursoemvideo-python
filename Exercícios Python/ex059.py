from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1,num2,soma))
    elif opção == 2:
        multiplicar = num1 * num2
        print('A multiplicação entre {} X {} é {}'.format(num1,num2,multiplicar))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num1,num2,maior))
    elif opção == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    print('=-='*10)
print('Fim do programa ! Volte sempre !')
