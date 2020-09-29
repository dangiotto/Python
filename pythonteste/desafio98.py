from time import sleep
def contador(i, f, p):
    print('=-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início : '))
fim = int(input('Fim    : '))
pas = int(input('Passo  : '))
contador(ini, fim, pas)



