times = ('Internacional', 'Galo', 'São Paulo', 'Flamengo', 'Palmeiras',
         'Santos', 'Vasco', 'Flu', 'Ceará', 'Fortaleza', 'Atlético Goianinse',
         'Grêmio', 'CAP', 'Sport', 'Corinthians', 'Bahia', 'Botafogo',
         'Goias', 'Coritiba', 'Bragantino')
print('=-='*20)
print(f'Os cinco primeiros times são:', times[0:5])
print('=-='*20)
print(f'Os últimos quatro times são:', times[-4:])
print('=-='*20)
print(f'Os times em ordem alfabética são:', sorted(times))
print('=-='*20)
print(f'O Santos está na {times.index("Santos")+1}ª colocação.')
print('=-='*20)