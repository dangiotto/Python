listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compaso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print ('{:.<20}'.format(listagem[c]),end='R$')
    if c % 2 != 0:
        print('{:>7.2f}'.format(listagem[c]))
print('-'*30)