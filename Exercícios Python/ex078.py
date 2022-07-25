numeros = []
mai = 0
men = 0
for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
    if c == 0:
        mai = men = numeros[c]
    else:
        if numeros[c] > mai:
            mai = numeros[c]
        if numeros[c] < men:
            men = numeros[c]
print('-'*30)            
print(f'Você digitou os valores {numeros}')
print(f'O maior número da lista é {mai} na posição ', end='')
for i,v in enumerate(numeros ):
    if v == mai:
        print(f'{i}... ',end='')
print()
print(f'O menor número da lista é {men} na posição ', end='')
for i,v in enumerate(numeros ):
    if v == men:
        print(f'{i}... ',end='')
print()
