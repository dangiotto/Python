from random import randint
c = 0
print('=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*20)
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(1,10)
    op = str(input('Par ou Ímpar ? [P/I]')).strip().upper()
    soma = jogador + pc
    print(f'Você escolheu {jogador} e o computador {pc}. Total de {soma}',end='')
    print(' DEU PAR\n' if soma % 2 ==0 else ' DEU IMPAR\n')
    if op == 'P' and soma % 2 == 0 or op == 'I' and soma % 2 != 0:
        print('-'*60)
        print('Você VENCEU!!!\nVamos jogar novamente...')
        print('=-='*20)
        c += 1
    else:
        print('-'*60)
        print('Você PERDEU!!')
        print(f'=-='*20,'\n\nGAME OVER! Você venceu {c} vezes.')
        break



