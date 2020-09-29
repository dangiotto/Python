from random import choice
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
print('=-='*20)
print('JOKENPÔ GAME')
print('=-='*20)
print('''ESCOLHA UMA DAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
player = int(input('Informe a sua escolha: '))
pc = choice(escolhas) #Poderia ser uma variável recebendo randint(0,2) e chamando escolhas[variável]
if player == 1:
    player = 'PEDRA'
    if player == pc:
        print('Empate!! Jogador escolheu: {} e PC: {}.'.format(player, pc))
    elif pc == 'PAPEL':
        print('Você perdeu!! Escolheu {}: e PC: {}.'.format(player, pc))
    else:
        print('Você ganhou!! Escolheu {}: e PC: {}.'.format(player, pc))
elif player == 2:
    player = 'PAPEL'
    if player == pc:
        print('Empate!! Jogador escolheu: {} e PC: {}.'.format(player, pc))
    elif pc == 'TESOURA':
        print('Você perdeu!! Escolheu: {} e PC: {}.'.format(player, pc))
    else:
        print('Você ganhou!! Escolheu: {} e PC: {}.'.format(player, pc))
elif player == 3:
    player = 'TESOURA'
    if player == pc:
        print('Empate!! Jogador escolheu: {} e PC: {}.'.format(player, pc))
    elif pc == 'PEDRA':
        print('Você perdeu!! Escolheu: {} e PC: {}.'.format(player, pc))
    else:
        print('Você ganhou!! Escolheu: {} e PC: {}.'.format(player, pc))
else:
    print('Número inválido tente novamente.')



