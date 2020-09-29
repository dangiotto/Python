i = int(input('Informe sua idade : '))
if i<=9:
    print('Idade {} - Até 9 anos : MIRIM'.format(i))
elif i>9 and i<=14:
    print('Idade {} - Até 14 anos: INFANTIL'.format(i))
elif i>14 and i<=19:
    print('Idade {} - Até 19 anos : JUNIOR'.format(i))
elif i>19 and i<=20:
    print('Idade {} - Até 20 anos : SêNIOR'.format(i))
else:
    print('Idade {} - Acima : MASTER'.format(i))