velocidade_carro = float(input('Digite a velocidade do carro Km: '))
if(velocidade_carro > 80):
   multa = (velocidade_carro - 80)* 7
   print('Você foi multado ! Terá que pagar {:.0f} R$ de multa !'.format(multa))
print('Bom dia, dirija com cuidado !')