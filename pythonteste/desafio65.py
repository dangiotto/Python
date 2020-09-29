c = 1
soma = 0
maior = ''
menor = ''
n = int(input('Digite um número :'))
soma += n
maior = n
menor = n
op =str(input('Quer digitar outro número ?\n[S/N]\n')).strip().upper()
while op == 'S':
    n = int(input('Digite um número :'))
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    op = str(input('Quer digitar outro número ?\n[S/N]\n')).strip().upper()
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print('Média : {:.1f}'.format(soma/c))
print('FIM')
