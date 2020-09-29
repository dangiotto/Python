from time import sleep


def maior(* núm):
    print('=-='*20)
    print('Analisando os valores passados...')
    for i in núm:
        print(i, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(núm)} ao todo.')
    sleep(0.5)
    if len(núm) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(núm)}')


maior(1, 5, 6, 3, 9, 12)
maior(4, 6, 9, 3, 5)
maior(10, 34)
maior(30, 54, 100)
maior()