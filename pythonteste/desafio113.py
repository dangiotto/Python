def leiaint(num=0):
    from termcolor import colored
    while True:
        try:
            n = int(input(num))
        except:
            print(colored('ERRO!! Digite um número inteiro válido.', 'red'))
        else:
            return n
            break


def leiareal(num=0):
    from termcolor import colored
    while True:
        try:
            n = float(input(num))
        except:
            print(colored('ERRO!! Digite um número inteiro válido.', 'red'))
        else:
            return n    
            break

n = leiaint('Digite um número inteiro: ')
nr = leiareal('Digite um número real: ')
print(f'O inteiro foi {n} e o real foi {nr}')