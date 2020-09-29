jogadores = list()
estat = dict()
gols = list ()
tot = 0
while True:
    estat.clear()
    estat['nome'] = str(input('Nome do jogador : '))
    partidas = int(input(f'Quantas partidas o jogador {estat["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    estat['gols'] = gols[:]
    estat['total'] = sum(gols)
    jogadores.append(estat.copy())
    while True:
        opt = str(input('Quer continuar ? [S/N]')).upper().strip()
        if opt in 'SN':
            break
        print('ERRO! Responde apenas S ou N.')
    if opt == 'N':
        break
print('-'*30)
print(f'cod   nome           gols        total')
for p, r in enumerate(jogadores):
    print(f'{p:>1}', end='     ')
    for v in r.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    opt = int(input('Mostrar dado de qual jogador? '))
    if opt == 999:
        break
    if opt >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {opt}.')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {jogadores[opt]["nome"]}: ')
    for p, r in enumerate(jogadores[opt]['gols']):
        print(f'   No jogo {p+1} fez {r} gols.')
    print('-'*40)
print(f'{"<<VOLTE SEMPRE>>":^15}')

