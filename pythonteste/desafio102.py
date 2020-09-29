def fatorial(n, show=False):
    """
    ---> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (Opcional) Exibe a operação matemática
    :return: O valor fatorial de um número n
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show is True:    #ou if show:
            print(f'{i}',end=' ')
            if i != 1:
                print('x', end=' ')
            if i ==1:
                print('=', end=' ')
    return print(f'{f}')


fatorial(5, show=True)
help(fatorial)

