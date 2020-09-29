def ficha(j='<desconhecido>', g=0):
    print(f'O jogador {j} fez : {g} gol(s)')


jogador = str(input("Type the player's name: "))
gols = str(input('How many goals did he score? :'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador, gols)