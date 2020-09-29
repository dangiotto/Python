def leiaint(num):
    from termcolor import colored
    while True:
        n = input(str(num))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(colored('ERRO!! Digite um número inteiro válido.', 'red'))
    return n

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')