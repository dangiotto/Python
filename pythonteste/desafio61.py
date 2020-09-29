from termcolor import colored
n=int(input('Informe o número : '))
r = int(input('Informe a razão : '))
c = 1
while c < 11:
    print('{} '.format(n),end='')
    n += r
    c += 1
print(colored('\nQuer que mostre mais algum termo? [S/N] ', 'red'))
op = str(input(colored('Digite a opção: ', 'yellow'))).upper().strip()
if op == 'S':
    t = int(input(colored('Mais quantos termos ?','red')))
    while c < 11+t:
        print('{} '.format(n), end='')
        n += r
        c += 1
else:
    print('FIM DO PROGRAMA')

