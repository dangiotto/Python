'''from random import choice
n = [0,1, 2, 3, 4, 5]
ns = (choice(n))
print ('=-=-=-=-=-=-=-=-=')
e = int(input('Escolha um némuro de 0 a 5 :\n'))
print('Numero escolhido pelo PC foi {} e você digitou {}'.format(ns,e))
print('Parabéns você ganhou!!' if ns == e else 'Você perdeu!!')'''

from random import randint
from time import sleep
from termcolor import colored
pc = randint(0, 5) #faz o pc pensar
print(colored('=-='*20,'yellow'))
print(colored('Vou pensar em um núemro de 0 a 5, tente advinhar...','blue'))
print(colored('=-='*20,'yellow'))
jg = int(input('Em que númeor eu pensei ?\n')) #jogador tenta advinhar
print(colored('Processando...','red'))
sleep(2)
print('Parabéns você ganhou!' if pc == jg else 'Você errou NOOB!! Eu pensei no número {}'.format(pc))