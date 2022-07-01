import math
angulo = float(input('Digite um número:'))
seno = math.sin(math.radians(angulo))
print('O Angulo de {} tem SENO de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O Angulo de {} tem o COSSENO {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE {:.2f}'.format(angulo,tangente))