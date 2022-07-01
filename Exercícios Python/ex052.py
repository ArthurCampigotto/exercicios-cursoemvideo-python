num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m',end=' ')
        tot += 1
    else:
        print('\033[1;33m',end=' ')
    print('{}'.format(c), end=' ')
print('O número {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')