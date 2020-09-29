from random import randint
from time import sleep


def sorteio(lst):
    for i in range(0, 5):
        lst.append(randint(0, 10))
        print(lst[i], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lst} temos : {soma}.')


numeros = list()
sorteio(numeros)
somaPar(numeros)