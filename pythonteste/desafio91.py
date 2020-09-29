from random import randint
from time import sleep
from operator import itemgetter
sorte = {}
raking = list()
for i in range (0,4):
    sorte[f'jogador{i+1}'] = randint(1, 6)
ranking = sorted(sorte.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados :')
for k, v in sorte.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('Ranking dos jogadores: ')
for p, v in enumerate(ranking):
    print(f'{p+1}º Lugar : {v[0]} com {v[1]}.')
    sleep(1)

