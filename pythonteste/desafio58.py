from random import randint
from time import sleep
from termcolor import colored
tent = 0
pc = randint(0, 5) #faz o pc pensar
print(colored('=-='*20,'yellow'))
print(colored('Vou pensar em um núemro de 0 a 5, tente advinhar...','blue'))
print(colored('=-='*20,'yellow'))
jg = int(input('Em que númeor eu pensei ?\n')) #jogador tenta advinhar
print(colored('Processando...','red'))
sleep(2)
while pc != jg:
    print(colored('ERROU!! Tente novamente','blue'))
    jg = int(input('Em que número eu pensei ?\n'))
    sleep(2)
    tent += +1
    if jg == pc:
        print('Parabéns você ganhou!')
        print('E tentou {} vezes'.format(tent))
