num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite ultimo número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O número 3 não foi digítado')
print(f'Os valores pares digitados foram ', end='')

for n in num:
    if n % 2 == 0:
        print(n,end= ' ')
