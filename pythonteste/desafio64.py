c = 0
soma = 0
n =int(input('Digite um número : '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite outro número ou (999) para sair: '))
print('''FIM
Quantidade de números digitados {}
Soma dos números digitdos {}'''.format(c, soma))