n = int(input('Informe o primeiro número de uma PA: '))
r = int(input('Informe a razão da PA : '))
#decimo = n + (10-1) * r
for i in range(0,10): # ou .....range(n, decimo , r):
    print('{}'.format(n), end = '-> ')
    n += r
print('Acabou!!')