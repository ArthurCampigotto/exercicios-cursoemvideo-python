times = ('Corinthinas','Palmeiras','Santos','Grêmio',
         'Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia',
         'São Paulo','Fluminense','Sport','Vitória',
         'Coritiba','Avaí','Ponte Preta','Atlético-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados {times[16:20]}')
print('-='*15)
print(f'Lista de times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1} posição')