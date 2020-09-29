
def ajuda(com, cor=0):
    print(c[cor], end='')
    help(com)
    print(c[0], end='')



def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

#pricipal
c = ('\033[m',          #sem cores
     '\033[0;30;41m',   #vermelho
     '\033[32;40m',     #verde
     '\033[30;43m',     #branco fundo amarelo
     )

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando, 3)
titulo('ATÉ LOGO!!', 2)
