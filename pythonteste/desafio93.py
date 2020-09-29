estat = dict()
gols = list ()
tot = 0
estat['nome'] = str(input('Nome do jogador : '))
partidas = int(input('Quantas partidas ele jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
estat['gols'] = gols[:]
estat['total'] = sum(gols)
print('=-='*20)
for k , v in estat.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-='*20)
print(f'O jogador {estat["nome"]} jogou {len(estat["gols"])} partidas.')
for p, v in enumerate(gols):
    print(f'     Na partida {p}, fez {v} gols.')
print(f'Foi um total de {estat["total"]} gols.')

