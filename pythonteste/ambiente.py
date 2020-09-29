'''def contador(i , f, p):
    """
    ---> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)'''

try:
    a = int(input('Denominador: '))
    b = int(input('Divisor: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar dados.')
else:
    print(f'A divisão é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')