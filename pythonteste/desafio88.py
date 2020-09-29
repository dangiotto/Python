from random import randint
from time import sleep
jogos = list()
num = list ()
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, qtd):
    while len(num) < 6:
        num.append(randint(1, 60))
        if num.count(num[len(num)-1]) == 2:
            num.pop()
    num.sort()
    jogos.append(num[:])
    num.clear()
print('=-='*4, f'SORTEANDO {qtd} JOGOS', '=-=' * 4)
sleep(1)
for i in range (0, qtd):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(1)
print('-'*6,'<BOA SORTE>','-'*6)





