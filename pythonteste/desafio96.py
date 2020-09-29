def area(a, b):
    a2 = a * b
    print(f'A área de {a}x{b} é igual a {a2}m².')


print(f'{"CONTROLE DE TERENOS":^30}')
print('-'*30)
l = float(input('LARGURA(m) :'))
c = float(input('COMPRIMENTO (m) : '))
area(l ,c)