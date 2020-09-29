from termcolor import colored
n1 = float(input(colored('Informe o primeiro número: ','yellow')))
n2 = float(input(colored('Informe o segundo número: ','yellow')))
print(colored('''-------MENU-------
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DA PÁGINA''','blue'))
op= int(input(colored('Escolha a opção :', 'red')))
while op != 5:
    while op == 4:
        n1 = float(input(colored('Informe o primeiro número: ', 'yellow')))
        n2 = float(input(colored('Informe o segundo número: ', 'yellow')))
        print(colored('''-------MENU-------
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DA PÁGINA''', 'blue'))
        op = int(input(colored('Escolha a opção :', 'red')))
    if op ==1:
        print('A soma é : {}'.format(n1 + n2))
        print(colored('''-------MENU-------
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DA PÁGINA''', 'blue'))
        op = int(input(colored('Escolha a opção :', 'red')))
    if op ==2:
        print('A multiplicação é {}'.format(n1*n2))
        print(colored('''-------MENU-------
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DA PÁGINA''', 'blue'))
        op = int(input(colored('Escolha a opção :', 'red')))
    if op ==3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            print(colored('''-------MENU-------
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4] NOVOS NÚMEROS
            [5] SAIR DA PÁGINA''', 'blue'))
            op = int(input(colored('Escolha a opção :', 'red')))
        else:
            print('{} é maior que {}'.format(n2, n1))
            print(colored('''-------MENU-------
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4] NOVOS NÚMEROS
            [5] SAIR DA PÁGINA''', 'blue'))
            op = int(input(colored('Escolha a opção :', 'red')))
print ('FIM DO PROGRAMA')