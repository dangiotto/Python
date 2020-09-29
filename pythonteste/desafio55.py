mais = 0
menos = 0
for c in range (1,6):
    peso = float(input('Informe o peso da {}ª pessoa : '.format(c)))
    if c == 1:
        mais = peso
        menos = peso
    else:
        if peso > mais:
            mais = peso
        else:
            menos = peso
print('A pessoa mais pesada tem {} KG.'.format(mais))
print('A pessoa mais leve tem {} KG'.format(menos))
