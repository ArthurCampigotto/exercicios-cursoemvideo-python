idade = int(input('Digite sua idade: '))
passou = idade - 18
falta = idade - 18

if(idade > 18):
    print('Seu tempo de alistamento éra a {} anos atrás'.format(passou))
elif(idade < 18):
    print('Seu tempo de alistamento é daqui a {} anos'.format(abs(falta)))
else:   
    print('O seu alistamento é esse ano !')
